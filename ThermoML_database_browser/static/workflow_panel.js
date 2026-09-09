/* Workflow (compaction Sankey) browser panel.
 * Renders the grouped figure listing produced by
 * agent_runner.list_workflow_figures() into a container: per-group
 * thumbnail grids; a click opens the interactive plotly HTML in a new
 * tab (falls back to the PNG); edge TSVs download inline. Shared by the
 * live launch pane (agents.html) and the run history page. */
(function () {
  'use strict';

  function fileUrl(opts, name) {
    let url = '/agents/workflow/' +
      encodeURIComponent(opts.agentType) + '/' +
      encodeURIComponent(opts.dirName) + '/' + encodeURIComponent(name) +
      '?scope=' + encodeURIComponent(opts.scope || 'all');
    if (opts.subRun) url += '&sub_run=' + encodeURIComponent(opts.subRun);
    return url;
  }

  function auditBadge(audit) {
    if (!audit) return null;
    const wrap = document.createElement('div');
    wrap.className = 'mb-3 d-flex align-items-center gap-2 flex-wrap';
    const label = document.createElement('span');
    label.className = 'small text-muted';
    label.textContent = 'Orphan audit (connectivity of every branch to the final answer/deliverable):';
    wrap.appendChild(label);
    const entries = [
      ['FAIL', 'bg-danger', 'broken / severed connections'],
      ['WARN', 'bg-warning text-dark', 'suspicious id flows'],
      ['INFO', 'bg-secondary', 'fully rejected branches (allowed)'],
    ];
    entries.forEach(function (entry) {
      const count = (audit[entry[0]] || 0);
      const badge = document.createElement('span');
      badge.className = 'badge ' + (count && entry[0] === 'FAIL' ? 'bg-danger' : count ? entry[1] : 'bg-success');
      badge.title = entry[2];
      badge.textContent = entry[0] + ' ' + count;
      wrap.appendChild(badge);
    });
    return wrap;
  }

  function render(container, workflow, opts) {
    container.innerHTML = '';
    if (!workflow || !(workflow.groups || []).length) {
      container.innerHTML =
        '<p class="text-muted mb-0">No workflow artifacts for this run. ' +
        'Workflow figures are generated after supported agent runs complete.</p>';
      return;
    }
    const badge = auditBadge(workflow.audit);
    if (badge) container.appendChild(badge);

    (workflow.groups || []).forEach(function (group) {
      const header = document.createElement('h6');
      header.className = 'mt-3 mb-2 border-bottom pb-1';
      header.innerHTML = '<i class="bi bi-diagram-3"></i> ';
      header.appendChild(document.createTextNode(group.name +
        ' (' + group.figures.length + ')'));
      container.appendChild(header);

      const row = document.createElement('div');
      row.className = 'row g-3';
      group.figures.forEach(function (figure) {
        const col = document.createElement('div');
        col.className = 'col-12 col-md-6 col-xl-4';
        const card = document.createElement('div');
        card.className = 'card h-100 shadow-sm';

        const img = document.createElement('img');
        img.src = fileUrl(opts, figure.png);
        img.alt = figure.label;
        img.className = 'card-img-top';
        img.loading = 'lazy';
        img.style.cursor = 'zoom-in';
        img.style.objectFit = 'contain';
        img.style.maxHeight = '220px';
        img.style.background = '#fff';
        img.title = figure.html
          ? 'Open the interactive Sankey in a new tab'
          : 'Open the figure in a new tab';
        img.addEventListener('click', function () {
          window.open(fileUrl(opts, figure.html || figure.png), '_blank');
        });
        card.appendChild(img);

        const body = document.createElement('div');
        body.className = 'card-body py-2 px-3 d-flex justify-content-between align-items-center gap-2';
        const caption = document.createElement('span');
        caption.className = 'small fw-semibold text-truncate';
        caption.title = figure.png;
        caption.textContent = figure.label;
        body.appendChild(caption);
        const links = document.createElement('span');
        links.className = 'text-nowrap';
        if (figure.html) {
          const a = document.createElement('a');
          a.href = fileUrl(opts, figure.html);
          a.target = '_blank';
          a.className = 'btn btn-sm btn-outline-primary py-0 me-1';
          a.title = 'Interactive plotly Sankey';
          a.innerHTML = '<i class="bi bi-arrows-move"></i>';
          links.appendChild(a);
        }
        const p = document.createElement('a');
        p.href = fileUrl(opts, figure.png);
        p.target = '_blank';
        p.className = 'btn btn-sm btn-outline-secondary py-0';
        p.title = 'Full-size PNG';
        p.innerHTML = '<i class="bi bi-image"></i>';
        links.appendChild(p);
        body.appendChild(links);
        card.appendChild(body);
        col.appendChild(card);
        row.appendChild(col);
      });
      container.appendChild(row);
    });

    if ((workflow.tsv_files || []).length) {
      const details = document.createElement('details');
      details.className = 'mt-3 small';
      const summary = document.createElement('summary');
      summary.className = 'text-muted';
      summary.textContent = 'OriginPro edge tables + audit report (' +
        workflow.tsv_files.length + ' TSV files)';
      details.appendChild(summary);
      const list = document.createElement('div');
      list.className = 'd-flex flex-wrap gap-2 mt-2';
      workflow.tsv_files.forEach(function (name) {
        const a = document.createElement('a');
        a.href = fileUrl(opts, name);
        a.className = 'badge text-bg-light text-decoration-none border';
        a.innerHTML = '<i class="bi bi-filetype-tsv"></i> ';
        a.appendChild(document.createTextNode(name));
        list.appendChild(a);
      });
      details.appendChild(list);
      container.appendChild(details);
    }
  }

  window.ThermoMLWorkflowPanel = { render: render };
})();
