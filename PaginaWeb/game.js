const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Auto
let car = {
  x: 400,
  y: 250,
  width: 40,
  height: 20,
  speed: 0,
  maxSpeed: 5,
  angle: 0
};

// Teclas
let keys = {};

document.addEventListener("keydown", e => keys[e.key] = true);
document.addEventListener("keyup", e => keys[e.key] = false);

function update() {

  // Acelerar
  if (keys["ArrowUp"]) {
    car.speed = Math.min(car.speed + 0.1, car.maxSpeed);
  }

  // Frenar
  if (keys["ArrowDown"]) {
    car.speed = Math.max(car.speed - 0.1, -2);
  }

  // Girar
  if (keys["ArrowLeft"]) car.angle -= 0.05;
  if (keys["ArrowRight"]) car.angle += 0.05;

  // Movimiento
  car.x += Math.cos(car.angle) * car.speed;
  car.y += Math.sin(car.angle) * car.speed;

  // Límites
  car.x = Math.max(0, Math.min(canvas.width, car.x));
  car.y = Math.max(0, Math.min(canvas.height, car.y));
}

function drawCar() {
  ctx.save();
  ctx.translate(car.x, car.y);
  ctx.rotate(car.angle);

  ctx.fillStyle = "red";
  ctx.fillRect(-car.width/2, -car.height/2, car.width, car.height);

  ctx.restore();
}

function drawTrack() {
  ctx.fillStyle = "#333";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function gameLoop() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawTrack();
  update();
  drawCar();
  requestAnimationFrame(gameLoop);
}

gameLoop();
