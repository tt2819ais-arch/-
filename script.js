const orbs = document.querySelectorAll(".orb");

window.addEventListener("pointermove", (event) => {
  const { innerWidth, innerHeight } = window;
  const offsetX = (event.clientX / innerWidth - 0.5) * 20;
  const offsetY = (event.clientY / innerHeight - 0.5) * 20;

  orbs.forEach((orb, index) => {
    const factor = (index + 1) * 0.6;
    orb.style.transform = `translate(${offsetX * factor}px, ${offsetY * factor}px)`;
  });
});
