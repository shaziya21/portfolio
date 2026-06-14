const API = {
  async signup(email, password) {
    const res = await fetch("/api/auth/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Signup failed");
    return data;
  },

  async login(email, password) {
    const body = new URLSearchParams({ username: email, password });
    const res = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body,
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Login failed");
    return data;
  },

  async getExperiences() {
    const res = await fetch("/api/experiences");
    return res.json();
  },

  async createExperience(payload) {
    const res = await fetch("/api/experiences", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Failed to create experience");
    return data;
  },

  async deleteExperience(id) {
    const res = await fetch(`/api/experiences/${id}`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    });
    if (!res.ok) {
      const data = await res.json();
      throw new Error(data.detail || "Failed to delete");
    }
  },
};

function setToken(token) {
  localStorage.setItem("token", token);
}

function clearToken() {
  localStorage.removeItem("token");
}

function getToken() {
  return localStorage.getItem("token");
}

function showAlert(el, message, type = "error") {
  el.textContent = message;
  el.className = `alert alert-${type}`;
  el.classList.remove("hidden");
}

function hideAlert(el) {
  el.classList.add("hidden");
}

document.addEventListener("DOMContentLoaded", () => {
  initAuthForms();
  initDashboard();
});

function initAuthForms() {
  const signupForm = document.getElementById("signup-form");
  if (signupForm) {
    signupForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const alert = document.getElementById("auth-alert");
      hideAlert(alert);

      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      try {
        const data = await API.signup(email, password);
        setToken(data.access_token);
        window.location.href = "/dashboard";
      } catch (err) {
        showAlert(alert, err.message);
      }
    });
  }

  const loginForm = document.getElementById("login-form");
  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const alert = document.getElementById("auth-alert");
      hideAlert(alert);

      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      try {
        const data = await API.login(email, password);
        setToken(data.access_token);
        window.location.href = "/dashboard";
      } catch (err) {
        showAlert(alert, err.message);
      }
    });
  }

  const logoutBtn = document.getElementById("logout-btn");
  if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
      clearToken();
      window.location.href = "/login";
    });
  }
}

function initDashboard() {
  const form = document.getElementById("experience-form");
  if (!form) return;

  if (!getToken()) {
    window.location.href = "/login";
    return;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const alert = document.getElementById("dashboard-alert");
    hideAlert(alert);

    const payload = {
      title: document.getElementById("exp-title").value,
      company: document.getElementById("exp-company").value,
      location: document.getElementById("exp-location").value,
      start_date: document.getElementById("exp-start").value,
      end_date: document.getElementById("exp-end").value || "Present",
      description: document.getElementById("exp-description").value,
      highlights: document.getElementById("exp-highlights").value,
    };

    try {
      await API.createExperience(payload);
      showAlert(alert, "Experience added successfully.", "success");
      form.reset();
      setTimeout(() => window.location.reload(), 800);
    } catch (err) {
      if (err.message.includes("credentials") || err.message.includes("401")) {
        clearToken();
        window.location.href = "/login";
        return;
      }
      showAlert(alert, err.message);
    }
  });

  document.querySelectorAll("[data-delete-id]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const id = btn.dataset.deleteId;
      if (!confirm("Delete this experience?")) return;

      try {
        await API.deleteExperience(id);
        btn.closest(".experience-card").remove();
      } catch (err) {
        const alert = document.getElementById("dashboard-alert");
        showAlert(alert, err.message);
      }
    });
  });
}
