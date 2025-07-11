document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('darkModeToggle');
  const body = document.body;

  function updateIcon(isDark) {
    toggle.textContent = isDark ? '☀️' : '🌙';
  }

  let isDark = localStorage.getItem('dark-mode') === 'enabled';
  if (isDark) {
    body.classList.add('dark-mode');
    updateIcon(true);
  }

  toggle.addEventListener('click', () => {
    isDark = !body.classList.contains('dark-mode');
    body.classList.toggle('dark-mode', isDark);
    localStorage.setItem('dark-mode', isDark ? 'enabled' : 'disabled');
    updateIcon(isDark);
  });
});
