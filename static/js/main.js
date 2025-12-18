// Utilidad: leer cookie
function getCookie(name){
  const v = `; ${document.cookie}`;
  const parts = v.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
  return "";
}

// Modo oscuro (solo alterna clase "alt" para variar el look)
const themeBtn = document.getElementById("themeBtn");
if (themeBtn) {
  const saved = localStorage.getItem("theme") || "default";
  if (saved === "alt") document.body.classList.add("alt");

  themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("alt");
    localStorage.setItem("theme", document.body.classList.contains("alt") ? "alt" : "default");
  });
}

// Filtro de tarjetas en Mensajes
const search = document.getElementById("search");
if (search) {
  search.addEventListener("input", () => {
    const q = search.value.toLowerCase().trim();
    document.querySelectorAll("[data-filter]").forEach(card => {
      const text = card.getAttribute("data-filter").toLowerCase();
      card.style.display = text.includes(q) ? "" : "none";
    });
  });
}

// Validación formulario + contador
const form = document.getElementById("contactForm");
if (form) {
  const nameEl = document.getElementById("name");
  const emailEl = document.getElementById("email");
  const msgEl = document.getElementById("content");
  const errorEl = document.getElementById("error");
  const counterEl = document.getElementById("counter");

  const MAX = 300;

  function updateCounter(){
    const n = msgEl.value.length;
    counterEl.textContent = `${n} / ${MAX}`;
    counterEl.style.color = n > MAX ? "var(--bad)" : "var(--muted)";
  }

  msgEl.addEventListener("input", updateCounter);
  updateCounter();

  form.addEventListener("submit", (e) => {
    errorEl.textContent = "";

    const name = nameEl.value.trim();
    const email = emailEl.value.trim();
    const msg = msgEl.value.trim();

    const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

    if (name.length < 2) {
      e.preventDefault();
      errorEl.textContent = "Tu nombre debe tener al menos 2 caracteres.";
      return;
    }
    if (!emailOk) {
      e.preventDefault();
      errorEl.textContent = "Ingresa un correo válido.";
      return;
    }
    if (msg.length < 10) {
      e.preventDefault();
      errorEl.textContent = "Tu mensaje debe tener al menos 10 caracteres.";
      return;
    }
    if (msg.length > MAX) {
      e.preventDefault();
      errorEl.textContent = `Tu mensaje no debe superar ${MAX} caracteres.`;
      return;
    }
  });
}
