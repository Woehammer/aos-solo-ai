import { useState } from 'react';
import UnitSidebar from '@/components/UnitSidebar';

export default function TestBattlePage() {
  const [playerUnits, setPlayerUnits] = useState([
    { name: 'Vampire Lord', modelCount: 1 },
    { name: 'Blood Knights', modelCount: 5 },
    { name: 'Vargheists', modelCount: 3 },
    { name: 'Skeletons', modelCount: 10 },
  ]);

  const [aiUnits, setAiUnits] = useState([
    { name: 'Killaboss on Gnashtoof', modelCount: 1 },
    { name: 'Man-skewer Boltboyz', modelCount: 3 },
    { name: 'Gutrippaz', modelCount: 10 },
  ]);

  const updatePlayerUnit = (index, change) => {
    setPlayerUnits(prev => {
      const updated = [...prev];
      updated[index].modelCount = Math.max(0, updated[index].modelCount + change);
      return updated;
    });
  };

  const updateAiUnit = (index, change) => {
    setAiUnits(prev => {
      const updated = [...prev];
      updated[index].modelCount = Math.max(0, updated[index].modelCount + change);
      return updated;
    });
  };

  return (
    <div className="flex flex-col md:flex-row gap-4 p-4">
      <UnitSidebar armyName="Soulblight Gravelords" allegiance="Death" units={playerUnits} onUpdateUnit={updatePlayerUnit} />
      <UnitSidebar armyName="Kruleboyz" allegiance="Destruction" units={aiUnits} onUpdateUnit={updateAiUnit} />
    </div>
  );
}
