const api = "http://127.0.0.1:5000/selcetInformation";

const inputElement = document.querySelector(".input");
const btnElement = document.querySelector(".btn");
const displaySection = document.querySelector(".display-section");
const percentEl = document.querySelector(".percent");
const inputLink = document.querySelector(".input-link");
const mess = document.querySelector(".message");
const name = document.querySelector(".name");
const avt = document.querySelector(".avatar");

const renderCirclePercent = (percent) => {
  return `<svg viewBox="0 0 36 36" class="circular-chart orange">
  <path class="circle-bg" d="M18 2.0845
      a 15.9155 15.9155 0 0 1 0 31.831
      a 15.9155 15.9155 0 0 1 0 -31.831" />
  <path class="circle" stroke-dasharray="${percent}, 100" d="M18 2.0845
      a 15.9155 15.9155 0 0 1 0 31.831
      a 15.9155 15.9155 0 0 1 0 -31.831" />
  <text x="18" y="20.35" class="percentage">${percent}%</text>
</svg>`;
};

const renderResult = (data) => {
  const { Name, Avatar, InputLink, Message, Percent } = data;
  percentEl.innerHTML = renderCirclePercent(Percent);
  inputLink.innerHTML = InputLink;
  mess.innerHTML = Message;
  name.innerHTML = Name;
  avt.style.backgroundImage = `url(${Avatar})`;
};

async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(data),
  });
  return await response.json();
}

inputElement.addEventListener("input", () => {
  displaySection.style.display = "none";
});

btnElement.onclick = async () => {
  const value = inputElement.value;
  const {data} = await postData(api, { InputLink: value });
  displaySection.style.display = "flex";
  renderResult(data);
  inputElement.value = "";
};
