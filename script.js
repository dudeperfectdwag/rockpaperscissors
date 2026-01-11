let playerScore = 0;
let computerScore = 0;
let isCooldown = false;

const playerScoreEl = document.getElementById('player-score');
const computerScoreEl = document.getElementById('computer-score');
const resultEl = document.getElementById('result');
const choicesEl = document.getElementById('choices');
const resetBtn = document.getElementById('reset');
const infoToggle = document.getElementById('info-toggle');
const infoModal = document.getElementById('info-modal');
const closeInfo = document.getElementById('close-info');

const roasts = [
  "Brutal execution 💀",
  "You got Vulcan nerve pinched",
  "Lizard ate your lunch",
  "Folded like cheap paper",
  "Rock crushed your dreams",
  "Spock mind-melded your brain",
  "Scissors snipped your hopes",
  "Ultimate skill issue detected",
  "Computer lives rent-free in your head"
];

const winPhrases = [
  "GOD MODE ACTIVATED 🔥",
  "You're unstoppable fr",
  "Computer ragequitting",
  "Peak strat execution",
  "Lizard/Spock MVP",
  "History made",
  "You're the chosen one",
  "Absolute domination"
];

const choices = ['rock', 'paper', 'scissors', 'lizard', 'spock'];

function getComputerChoice() {
  return choices[Math.floor(Math.random() * choices.length)];
}

function doesPlayerWin(playerChoice, computerChoice) {
  return (
    (playerChoice === 'rock' && (computerChoice === 'scissors' || computerChoice === 'lizard')) ||
    (playerChoice === 'paper' && (computerChoice === 'rock' || computerChoice === 'spock')) ||
    (playerChoice === 'scissors' && (computerChoice === 'paper' || computerChoice === 'lizard')) ||
    (playerChoice === 'lizard' && (computerChoice === 'paper' || computerChoice === 'spock')) ||
    (playerChoice === 'spock' && (computerChoice === 'rock' || computerChoice === 'scissors'))
  );
}

function startCountdownAndPlay(playerChoice) {
  if (isCooldown) return;

  isCooldown = true;
  choicesEl.classList.add('disabled');
  
  // Dramatic countdown
  resultEl.className = 'result-message cooldown';
  resultEl.textContent = 'Rock...';
  
  setTimeout(() => {
    resultEl.textContent = 'Paper...';
    
    setTimeout(() => {
      resultEl.textContent = 'Scissors...';
      
      setTimeout(() => {
        // Now reveal the result
        const computerChoice = getComputerChoice();
        let message = `Computer played ${computerChoice}... `;
        let outcomeClass = 'result-message';

        if (playerChoice === computerChoice) {
          message += "Tie! Replay the multiverse 🤝";
          outcomeClass += ' tie';
        } else if (doesPlayerWin(playerChoice, computerChoice)) {
          playerScore++;
          playerScoreEl.textContent = playerScore;
          message += winPhrases[Math.floor(Math.random() * winPhrases.length)];
          outcomeClass += ' win';
        } else {
          computerScore++;
          computerScoreEl.textContent = computerScore;
          message += roasts[Math.floor(Math.random() * roasts.length)];
          outcomeClass += ' lose';
        }

        resultEl.textContent = message;
        resultEl.className = outcomeClass;

        // Short delay before allowing next play
        setTimeout(() => {
          isCooldown = false;
          choicesEl.classList.remove('disabled');
        }, 1500); // 1.5s grace period after result (total ~4.5s per round)

      }, 1000);
      
    }, 1000);
    
  }, 1000);
}

document.querySelectorAll('.choice').forEach(button => {
  button.addEventListener('click', () => {
    const choice = button.dataset.choice;
    startCountdownAndPlay(choice);
  });
});

resetBtn.addEventListener('click', () => {
  playerScore = 0;
  computerScore = 0;
  playerScoreEl.textContent = '0';
  computerScoreEl.textContent = '0';
  resultEl.textContent = 'Choose your weapon...';
  resultEl.className = 'result-message';
  choicesEl.classList.remove('disabled');
  isCooldown = false;
});

// Modal controls (unchanged)
infoToggle.addEventListener('click', () => {
  infoModal.classList.add('active');
});

closeInfo.addEventListener('click', () => {
  infoModal.classList.remove('active');
});

infoModal.addEventListener('click', (e) => {
  if (e.target === infoModal) {
    infoModal.classList.remove('active');
  }
});