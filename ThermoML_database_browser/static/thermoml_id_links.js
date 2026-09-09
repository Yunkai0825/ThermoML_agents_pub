/**
 * thermoml_id_links.js — link ThermoML identifiers in rendered agent output
 * to their specific browser pages.
 *
 *   DOI            -> /paper/<doi>
 *   GLOBlit_N      -> /lit/GLOBlit_N            (302 -> paper page)
 *   PROP/RXNblock_N-> its GLOBlit_X::block pairing (ledger/citations) when
 *                     unambiguous, else nearest preceding lit/DOI context:
 *                     /lit/GLOBlit_N?block=...  or /paper/<doi>#block-...
 *   GLOBcomp_N     -> /comp/GLOBcomp_N          (302 -> compound page)
 *
 * GLOB(prop|var|meas|constr) are deliberately left alone — the agents page
 * binds those to the entity-card modal instead.
 *
 * Usage: ThermoIDLinks.linkify(element)  — after innerHTML assignment.
 * Walks text nodes only, so existing anchors are never double-linked.
 */
(function () {
  "use strict";

  var DOI_RE = /\b10\.\d{4,9}\/[^\s`|)<>,;\]"']+/g;
  var TOKEN_RE = /\b(10\.\d{4,9}\/[^\s`|)<>,;\]"']+|GLOBlit_[1-9]\d*|GLOBcomp_[1-9]\d*|(?:PROP|RXN)block_[1-9]\d*)\b/g;
  var PAIR_RE = /\b(GLOBlit_[1-9]\d*)\s*::\s*((?:PROP|RXN)block_[1-9]\d*)\b/g;
  var SKIP_TAGS = { A: 1, SCRIPT: 1, STYLE: 1, CODE: 0, PRE: 0, TEXTAREA: 1 };

  function pfx(u) {
    return u;
  }

  function stripTrail(doi) {
    return doi.replace(/[.,;:]+$/, "");
  }

  function makeLink(href, text, title) {
    var a = document.createElement("a");
    a.href = pfx(href);
    a.textContent = text;
    a.className = "thermoml-id-link";
    a.title = title;
    a.target = "_blank";
    a.rel = "noopener";
    return a;
  }

  function linkFor(token, ctx) {
    if (token.lastIndexOf("10.", 0) === 0) {
      var doi = stripTrail(token);
      ctx.doi = doi;
      return makeLink("/paper/" + encodeURI(doi), token, "Open paper " + doi);
    }
    if (token.lastIndexOf("GLOBlit_", 0) === 0) {
      ctx.lit = token;
      return makeLink("/lit/" + token, token, "Open paper " + token);
    }
    if (token.lastIndexOf("GLOBcomp_", 0) === 0) {
      return makeLink("/comp/" + token, token, "Open compound " + token);
    }
    // block token — prefer the document's authoritative GLOBlit_N::block
    // pairing (e.g. from the evidence-ledger captions), then fall back to
    // the nearest preceding lit/DOI context.
    var paired = ctx.pairs && ctx.pairs[token];
    if (paired) {
      return makeLink("/lit/" + paired + "?block=" + token, token,
                      "Open " + token + " of " + paired);
    }
    if (ctx.lit) {
      return makeLink("/lit/" + ctx.lit + "?block=" + token, token,
                      "Open " + token + " of " + ctx.lit);
    }
    if (ctx.doi) {
      return makeLink("/paper/" + encodeURI(ctx.doi) + "#block-" + token, token,
                      "Open " + token + " of " + ctx.doi);
    }
    return null;
  }

  function collectQualifiedPairs(root) {
    // Map block token -> lit token from explicit qualified citations;
    // conflicting pairings (same block id under two papers) stay unmapped
    // so the running-context heuristic decides those.
    var pairs = {};
    var text = root.textContent || "";
    PAIR_RE.lastIndex = 0;
    var m;
    while ((m = PAIR_RE.exec(text)) !== null) {
      if (pairs[m[2]] === undefined) pairs[m[2]] = m[1];
      else if (pairs[m[2]] !== m[1]) pairs[m[2]] = null;
    }
    return pairs;
  }

  function processTextNode(node, ctx) {
    var text = node.nodeValue;
    TOKEN_RE.lastIndex = 0;
    if (!TOKEN_RE.test(text)) return;
    TOKEN_RE.lastIndex = 0;
    var frag = document.createDocumentFragment();
    var last = 0, m;
    while ((m = TOKEN_RE.exec(text)) !== null) {
      var link = linkFor(m[1], ctx);
      if (!link) continue;
      frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      frag.appendChild(link);
      last = m.index + m[1].length;
    }
    if (last === 0) return;
    frag.appendChild(document.createTextNode(text.slice(last)));
    node.parentNode.replaceChild(frag, node);
  }

  function linkify(root) {
    if (!root) return;
    // Collect text nodes and pre-existing anchors in document order first;
    // context (last lit/DOI seen) must advance during processing, not during
    // the walk, so block tokens attach to the source line they belong to.
    var items = [];
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_ALL, {
      acceptNode: function (n) {
        if (n.nodeType === 1) {
          if (SKIP_TAGS[n.tagName]) {
            if (n.tagName === "A") items.push({ anchor: n.textContent || "" });
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_SKIP;
        }
        return n.nodeType === 3 ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
      },
    });
    while (walker.nextNode()) items.push({ text: walker.currentNode });

    var ctx = { lit: null, doi: null, pairs: collectQualifiedPairs(root) };
    for (var i = 0; i < items.length; i++) {
      if (items[i].anchor !== undefined) {
        var t = items[i].anchor;
        if (/^10\./.test(t)) ctx.doi = stripTrail(t);
        if (/^GLOBlit_\d+$/.test(t)) ctx.lit = t;
        continue;
      }
      processTextNode(items[i].text, ctx);
    }
  }

  window.ThermoIDLinks = { linkify: linkify };
})();
