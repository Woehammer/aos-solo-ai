import { useState } from 'react';

export default function UnitSidebar({ armyName, allegiance, units, onUpdateUnit }) {
  const colorMap = {
    Order: 'border-blue-500',
    Chaos: 'border-red-600',
    Death: 'border-black',
    Destruction: 'border-green-600',
  };

  return (
    <div className={`w-full p-3 rounded-xl border-4 ${colorMap[allegiance] || 'border-gray-400'} shadow-lg bg-white dark:bg-gray-900`}>
      <h2 className="text-xl font-bold mb-3 text-center">{armyName}</h2>
      <ul className="space-y-3">
        {units.map((unit, index) => (
          <li key={index} className="p-2 border rounded-md bg-gray-50 dark:bg-gray-800">
            <div className="flex justify-between items-center">
              <div>
                <p className="font-semibold">{unit.name}</p>
                <p className="text-sm text-gray-500">Models: {unit.modelCount}</p>
              </div>
              <div className="flex items-center space-x-2">
                <button
                  className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600"
                  onClick={() => onUpdateUnit(index, -1)}
                >–</button>
                <button
                  className="px-2 py-1 bg-green-500 text-white rounded hover:bg-green-600"
                  onClick={() => onUpdateUnit(index, 1)}
                >+</button>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
