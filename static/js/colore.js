  // Nasconde il messaggio di vittoria dopo 5 secondi
  setTimeout(function () {
    const vittoriaMsg = document.getElementById("vittoria-msg");
    if (vittoriaMsg) {
      vittoriaMsg.style.display = "none";
    }

    const messaggio = document.getElementById("messaggio");
    if (messaggio) {
      messaggio.style.display = "none";
    }
  }, 5000);

  function showContent() {
    document.getElementById("mainContent").style.display = "block";
  }