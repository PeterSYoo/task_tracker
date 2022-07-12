console.log('timer loaded')

// Global variables
const time_el = document.querySelector('.task--new .task--new-timer');
const start_btn = document.querySelector('.timer-start');
const stop_btn = document.querySelector('.timer-stop');
const reset_btn = document.querySelector('.timer-reset');

let seconds = 0;
let interval = null;

// Update the timer
const timer = () => {
  seconds++;

  // Format our time
  let hrs = Math.floor(seconds / 3600);
  let mins = Math.floor((seconds - (hrs * 3600)) / 60);
  let secs = seconds % 60;

  if (secs < 10) secs = '0' + secs;
  if (mins < 10) mins = '0' + mins;
  if (hrs < 10) hrs = '0' + hrs;

  time_el.innerText = `${hrs}:${mins}:${secs}`;
}

const start = () => {
  if (interval) {
    return
  }

  interval = setInterval(timer, 1000);
}

const stop = () => {
  clearInterval(interval);
  interval = null;
}

const reset = () => {
  stop();
  seconds = 0;
  time_el.innerText = '00:00:00';
}

// Event listeners
start_btn.addEventListener('click', start);
stop_btn.addEventListener('click', stop);
reset_btn.addEventListener('click', reset);