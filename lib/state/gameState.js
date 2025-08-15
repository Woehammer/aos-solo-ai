// Starter gameState.js (tracks unit models, objective control, etc.)

export const initialState = {
  turn: 1,
  round: 1,
  activePlayer: 'ai', // or 'human'
  initiativeRoll: null,
  objectives: [
    { id: 'dracothion', name: 'Dracothion Dias', heldBy: null },
    { id: 'ignax', name: 'Ignax Dias', heldBy: null },
    { id: 'behemat', name: 'Behemat Dias', heldBy: null },
    { id: 'vulcatrix', name: 'Vulcatrix Dias', heldBy: null },
    { id: 'agenda', name: 'Agenda Dias', heldBy: null },
  ],
  armies: {
    ai: {
      faction: 'kruleboyz',
      units: [
        { id: 'unit1', name: 'Killaboss', models: 1, maxModels: 1 },
        { id: 'unit2', name: 'Gutrippaz', models: 10, maxModels: 10 },
        // ...more units
      ],
    },
    human: {
      faction: 'soulblight',
      units: [
        { id: 'unit1', name: 'Vampire Lord', models: 1, maxModels: 1 },
        { id: 'unit2', name: 'Skeletons', models: 10, maxModels: 10 },
        // ...more units
      ],
    },
  },
  combatLog: [],
};

