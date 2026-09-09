(function (global) {
  'use strict';

  /**
   * Turn a result-panel tab strip into independent section toggles.
   *
   * Unlike Bootstrap tabs, more than one section may be active at once. The
   * controller keeps at least one section visible so the result panel cannot
   * be collapsed into an unexplained blank area.
   */
  function createResultPanelToggles(options) {
    if (!options || !options.root) {
      throw new TypeError('createResultPanelToggles requires a root element');
    }

    var root = options.root;
    var buttonSelector = options.buttonSelector || '[data-section]';
    var sectionSelector = options.sectionSelector || '.detail-section[data-section]';
    var buttons = Array.prototype.slice.call(root.querySelectorAll(buttonSelector));
    var sections = Array.prototype.slice.call(root.querySelectorAll(sectionSelector));
    var onSectionShown = typeof options.onSectionShown === 'function'
      ? options.onSectionShown
      : function () {};
    var allowEmpty = options.allowEmpty === true;
    var selected = new Set();

    if (!buttons.length || !sections.length) {
      throw new Error('result panel requires section buttons and section elements');
    }

    var knownSections = new Set(sections.map(function (element) {
      return element.dataset.section;
    }));

    function addKnown(section) {
      if (knownSections.has(section)) selected.add(section);
    }

    if (Array.isArray(options.initialSections)) {
      options.initialSections.forEach(addKnown);
    } else {
      buttons.forEach(function (button) {
        if (button.classList.contains('active')) addKnown(button.dataset.section);
      });
    }
    if (!selected.size) addKnown(buttons[0].dataset.section);

    function render() {
      buttons.forEach(function (button) {
        var active = selected.has(button.dataset.section);
        button.classList.toggle('active', active);
        button.setAttribute('aria-pressed', active ? 'true' : 'false');
      });
      sections.forEach(function (element) {
        var active = selected.has(element.dataset.section);
        element.classList.toggle('active', active);
        element.setAttribute('aria-hidden', active ? 'false' : 'true');
      });
    }

    function setVisible(section, visible) {
      if (!knownSections.has(section)) return false;
      var wasVisible = selected.has(section);
      if (visible) {
        selected.add(section);
      } else {
        if (!wasVisible) return false;
        if (!allowEmpty && selected.size === 1) return false;
        selected.delete(section);
      }
      render();
      if (visible && !wasVisible) onSectionShown(section);
      return true;
    }

    function toggle(section) {
      return setVisible(section, !selected.has(section));
    }

    buttons.forEach(function (button) {
      button.setAttribute('aria-pressed', 'false');
      button.addEventListener('click', function (event) {
        event.preventDefault();
        toggle(button.dataset.section);
      });
    });

    root.classList.add('multi-section-result-panel');
    render();
    Array.from(selected).forEach(onSectionShown);

    return {
      toggle: toggle,
      setVisible: setVisible,
      ensureVisible: function (section) { return setVisible(section, true); },
      selectedSections: function () { return Array.from(selected); }
    };
  }

  global.ThermoMLResultPanels = Object.freeze({
    createToggles: createResultPanelToggles
  });
})(window);
