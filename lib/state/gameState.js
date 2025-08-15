// gameState.js

const gameState = {
  round: 1,
  turn: 'Player', // 'Player' or 'AI'
  initiativeRolls: [],
  aiVictoryPoints: 0,
  playerVictoryPoints: 0,
  twistCard: null,
  battleTactic: null,
  selectedEnhancement: null,

  armies: {
    AI: {
      faction: null,
      name: null,
      units: [], // [{ name: 'Gutrippaz', models: 10, woundsPerModel: 2, currentModels: 10, isHero: false, ... }]
    },
    Player: {
      faction: null,
      name: null,
      units: []
    }
  },

  objectives: {
    dracothion: { name: 'Dracothion Dias', controlledBy: null, location: [0, 0] },
    ignax: { name: 'Ignax Dias', controlledBy: null, location: [0, 0] },
    behemat: { name: 'Behemat Dias', controlledBy: null, location: [0, 0] },
    vulcatrix: { name: 'Vulcatrix Dias', controlledBy: null, location: [0, 0] },
    agenda: { name: 'Agenda Dias', controlledBy: null, location: [0, 0] },
  },

  combatLog: [], // Array of objects with narrative combat or shooting descriptions

  updateVictoryPoints(player, points) {
    if (player === 'AI') {
      this.aiVictoryPoints += points;
    } else {
      this.playerVictoryPoints += points;
    }
  },

  setObjectiveControl(objectiveKey, controller) {
    if (this.objectives[objectiveKey]) {
      this.objectives[objectiveKey].controlledBy = controller;
    }
  },

  logCombatMessage(message) {
    this.combatLog.push({ round: this.round, turn: this.turn, message });
  },

  getCurrentScores() {
    return {
      AI: this.aiVictoryPoints,
      Player: this.playerVictoryPoints
    };
  },

  advanceTurn() {
    this.turn = this.turn === 'Player' ? 'AI' : 'Player';
    if (this.turn === 'Player') this.round += 1;
  },

  reset() {
    this.round = 1;
    this.turn = 'Player';
    this.aiVictoryPoints = 0;
    this.playerVictoryPoints = 0;
    this.combatLog = [];
    this.twistCard = null;
    this.battleTactic = null;
    this.selectedEnhancement = null;
    for (const key in this.objectives) {
      this.objectives[key].controlledBy = null;
    }
    this.armies.AI = { faction: null, name: null, units: [] };
    this.armies.Player = { faction: null, name: null, units: [] };
  }
};

export default gameState;
