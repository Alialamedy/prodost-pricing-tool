import { renderForm } from './components/form.js';
import { calculateCosts } from './logic/calculate.js';

window.calculateCosts = calculateCosts;

window.onload = () => {
  renderForm("app");
};
