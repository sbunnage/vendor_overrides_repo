async function loadOverrides() {
  const res = await fetch("/overrides");
  const data = await res.json();

  const list = document.getElementById("list");
  list.innerHTML = "";

  for (const [prefix, vendor] of Object.entries(data)) {
    const row = document.createElement("div");
    row.textContent = prefix + " → " + vendor;
    list.appendChild(row);
  }
}

async function saveOverride() {
  const prefix = document.getElementById("prefix").value;
  const vendor = document.getElementById("vendor").value;

  await fetch("/overrides", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({prefix, vendor})
  });

  loadOverrides();
}

window.onload = loadOverrides;
