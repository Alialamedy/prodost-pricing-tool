
// Production cost groups by paper size
const productionGroups = {
  'groupA': ['70x100', '64x90'],
  'groupB': ['50x70', '45x64', '33x70', '30x64'],
  'groupC': ['35x50', '32x45']
};

// Cost structure per group
const productionCosts = {
  groupA: {
    printing: 0.10,
    selefon: 0.08,
    lak: 0.05,
    cutting: 0.07,
    gluing: 0.10
  },
  groupB: {
    printing: 0.08,
    selefon: 0.06,
    lak: 0.04,
    cutting: 0.06,
    gluing: 0.08
  },
  groupC: {
    printing: 0.06,
    selefon: 0.04,
    lak: 0.03,
    cutting: 0.05,
    gluing: 0.06
  }
};

// Identify paper group
function getPaperGroup(size) {
  for (const [group, sizes] of Object.entries(productionGroups)) {
    if (sizes.includes(size)) return group;
  }
  return 'groupB'; // default fallback
}

// Calculate cost per piece
function calculateCosts(paperSize, options = {}) {
  const group = getPaperGroup(paperSize);
  const costs = productionCosts[group];

  const {
    quantity = 1000,
    applyLak = true,
    doubleLayer = false
  } = options;

  let unitCost = costs.printing + costs.selefon + costs.cutting + costs.gluing;
  if (applyLak) unitCost += costs.lak;
  if (doubleLayer) unitCost *= 2;

  const totalCost = unitCost * quantity;
  const costPerPiece = totalCost / quantity;

  return {
    group,
    unitCost: unitCost.toFixed(4),
    totalCost: totalCost.toFixed(2),
    costPerPiece: costPerPiece.toFixed(4)
  };
}

// Example usage
// const result = calculateCosts('70x100', { quantity: 2000, applyLak: true, doubleLayer: false });
// console.log(result);
