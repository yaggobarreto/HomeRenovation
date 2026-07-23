document.addEventListener('DOMContentLoaded', function () {
  var botao = document.querySelector('.topbar-menu-btn');
  var sidebar = document.querySelector('.sidebar');
  var overlay = document.querySelector('.sidebar-overlay');

  if (!botao || !sidebar || !overlay) return;

  function fechar() {
    sidebar.classList.remove('aberta');
    overlay.classList.remove('aberta');
  }

  botao.addEventListener('click', function () {
    sidebar.classList.toggle('aberta');
    overlay.classList.toggle('aberta');
  });

  overlay.addEventListener('click', fechar);
});
