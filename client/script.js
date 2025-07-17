fetch("/events")
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
  })

document.querySelector("form").addEventListener("submit"), (event) => {
  event.preventDefault();
  const title = document.querySelector("title").value
}

fetch("/events", {
  method: "POST",
  headers: {"Content-Type": "application/json" },
  body: JSON.stringify({ title })
})
.then(response => response.json())
.then(renderEvent)

function renderEvent(event) {
  const li = document.createElement("li");
  li.textContent = `${event.title}`
  document.querySelector("#product-list").appendChild(li)
}