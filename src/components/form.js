
export function renderForm(containerId) {
  const container = document.getElementById(containerId);
  container.innerHTML = `
    <h2>Prodost Fiyatlandırma Formu</h2>
    <label>Ürün Türü:
      <select id="productType">
        <option value="bristol">Bristol Kutu</option>
        <option value="sivamali">Sıvamalı Kutu</option>
        <option value="canta">Çanta</option>
      </select>
    </label>
    <label>Kağıt Boyutu:
      <select id="paperSize">
        <option value="70x100">70x100</option>
        <option value="64x90">64x90</option>
        <option value="50x70">50x70</option>
        <option value="45x64">45x64</option>
        <option value="33x70">33x70</option>
        <option value="30x64">30x64</option>
        <option value="35x50">35x50</option>
        <option value="32x45">32x45</option>
      </select>
    </label>
    <label>Adet:
      <input type="number" id="quantity" value="1000" />
    </label>
    <label>
      <input type="checkbox" id="applyLak" checked /> Lak Uygulansın mı?
    </label>
    <label>
      <input type="checkbox" id="doubleLayer" /> İkinci Katman Ekle
    </label>
    <button onclick="calculate()">Hesapla</button>
    <div id="resultBox"></div>
  `;
}

window.calculate = async function() {
  const paperSize = document.getElementById("paperSize").value;
  const quantity = parseInt(document.getElementById("quantity").value);
  const applyLak = document.getElementById("applyLak").checked;
  const doubleLayer = document.getElementById("doubleLayer").checked;

  const res = calculateCosts(paperSize, { quantity, applyLak, doubleLayer });
  document.getElementById("resultBox").innerHTML = `
    <p><strong>Grup:</strong> ${res.group}</p>
    <p><strong>Toplam Maliyet:</strong> ${res.totalCost} USD</p>
    <p><strong>Parça Başına Maliyet:</strong> ${res.costPerPiece} USD</p>
  `;
}
