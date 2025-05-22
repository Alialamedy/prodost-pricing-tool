import os
import json
from flask import Flask, render_template, request, jsonify

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "development_secret_key")

@app.route('/')
def index():
    """Render the main calculator page"""
    return render_template('index.html')

@app.route('/pricing')
def pricing():
    """Render the pricing configuration page"""
    return render_template('pricing.html')

@app.route('/save_pricing', methods=['POST'])
def save_pricing():
    """Save the pricing configuration to a file"""
    try:
        # Get the pricing configuration from the form
        config = request.json
        
        # Build JavaScript code to update pricing-config.js
        js_code = "// PRICING CONFIGURATION - Edit this file when prices change\n"
        js_code += "// =======================================================================\n\n"
        
        # Paper pricing constants
        js_code += "// Paper pricing constants\n"
        js_code += f"const PAPER_PRICE_MULTIPLIER = {config['paperPriceMultiplier']}; // Price multiplier for papers\n"
        js_code += f"const USD_TO_TL_DEFAULT = {config['usdToTlDefault']};        // Default USD to TL exchange rate\n\n"
        
        # Production cost constants
        js_code += "// Production cost constants (feel free to adjust these when prices change)\n"
        
        # Large paper sizes
        js_code += "// Large paper sizes (70x100, 64x90)\n"
        js_code += f"const LARGE_PAPER_BASKI_FIRST_BATCH = {config['largePaperBaskiFirstBatch']};     // Baski cost for first 1000 sheets\n"
        js_code += f"const LARGE_PAPER_BASKI_ADDITIONAL = {config['largePaperBaskiAdditional']};      // Baski cost for each additional 1000 sheets\n"
        js_code += f"const LARGE_PAPER_BICAK = {config['largePaperBicak']};                 // Bicak cost\n"
        js_code += f"const LARGE_PAPER_KESIM_FIRST_BATCH = {config['largePaperKesimFirstBatch']};     // Kesim cost for first 1300 sheets\n"
        js_code += f"const LARGE_PAPER_KESIM_ADDITIONAL = {config['largePaperKesimAdditional']};       // Kesim cost for each additional 1000 sheets\n\n"
        
        # Medium paper sizes
        js_code += "// Medium paper sizes (50x70, 45x64, 33x70, 30x64)\n"
        js_code += f"const MEDIUM_PAPER_BASKI_FIRST_BATCH = {config['mediumPaperBaskiFirstBatch']};    // Baski cost for first 1300 sheets\n"
        js_code += f"const MEDIUM_PAPER_BASKI_ADDITIONAL = {config['mediumPaperBaskiAdditional']};     // Baski cost for each additional 1000 sheets\n"
        js_code += f"const MEDIUM_PAPER_BICAK = {config['mediumPaperBicak']};                // Bicak cost\n"
        js_code += f"const MEDIUM_PAPER_KESIM_FIRST_BATCH = {config['mediumPaperKesimFirstBatch']};    // Kesim cost for first 1300 sheets\n"
        js_code += f"const MEDIUM_PAPER_KESIM_ADDITIONAL = {config['mediumPaperKesimAdditional']};      // Kesim cost for each additional 1000 sheets\n\n"
        
        # Small paper sizes
        js_code += "// Small paper sizes (35x50, 32x45)\n"
        js_code += f"const SMALL_PAPER_BASKI_FIRST_BATCH = {config['smallPaperBaskiFirstBatch']};     // Baski cost for first 1000 sheets\n"
        js_code += f"const SMALL_PAPER_BASKI_ADDITIONAL = {config['smallPaperBaskiAdditional']};       // Baski cost for each additional 1000 sheets\n"
        js_code += f"const SMALL_PAPER_BICAK = {config['smallPaperBicak']};                 // Bicak cost\n"
        js_code += f"const SMALL_PAPER_KESIM_FIRST_BATCH = {config['smallPaperKesimFirstBatch']};     // Kesim cost for first 1000 sheets\n"
        js_code += f"const SMALL_PAPER_KESIM_ADDITIONAL = {config['smallPaperKesimAdditional']};       // Kesim cost for each additional 1000 sheets\n\n"
        
        # LAK and Selefon constants
        js_code += "// LAK and Selefon constants\n"
        js_code += f"const SELEFON_MIN_COST = {config['selefonMinCost']};                   // Minimum cost for selefon\n"
        js_code += f"const SELEFON_M2_COST = {config['selefonM2Cost']};                    // Cost per m² for selefon\n\n"
        
        # LAK costs
        js_code += "// LAK costs for large papers\n"
        js_code += f"const LARGE_PAPER_LAK_BASE = {config['largePaperLakBase']};              // Base cost for LAK on large papers\n"
        js_code += f"const LARGE_PAPER_LAK_FILM = {config['largePaperLakFilm']};              // Film cost for LAK on large papers\n"
        js_code += "// LAK costs for small/medium papers\n"
        js_code += f"const SMALL_PAPER_LAK_BASE = {config['smallPaperLakBase']};              // Base cost for LAK on small/medium papers\n"
        js_code += f"const SMALL_PAPER_LAK_FILM = {config['smallPaperLakFilm']};               // Film cost for LAK on small/medium papers\n"
        js_code += f"const LAK_ADDITIONAL_SHEET_COST = {config['lakAdditionalSheetCost']};          // Additional cost per sheet over 1000\n\n"
        
        # Yapistirma base costs
        js_code += "// Yapistirma base costs - cost for first 1250 units\n"
        js_code += f"const YAPISTIRMA_EKLEMELI_BASE = {config['yapistirmaEklemeliBase']};          // Base cost for Eklemeli\n"
        js_code += f"const YAPISTIRMA_TEK_PARCA_BASE = {config['yapistirmaTekParcaBase']};         // Base cost for Tek Parça\n"
        js_code += f"const YAPISTIRMA_PASTANE_BASE = {config['yapistirmaPastaneBase']};           // Base cost for Pastane\n\n"
        
        # Ip Turu base costs
        js_code += "// Ip Turu base costs - cost for first 1250 units\n"
        js_code += f"const IP_BURGULU_BASE = {config['ipBurguluBase']};                   // Base cost for Burgulu\n"
        js_code += f"const IP_SATEN_BASE = {config['ipSatenBase']};                     // Base cost for Saten\n\n"
        
        # Other costs
        js_code += "// Other costs\n"
        js_code += f"const VARAK_KLISE_BUYUK = {config['varakKliseBuyuk']};                 // Cost for Buyuk Varak Klise\n"
        js_code += f"const VARAK_KLISE_UFAK = {config['varakKliseUfak']};                  // Cost for Ufak Varak Klise\n"
        js_code += f"const VARAK_BASKI_BASE = {config['varakBaskiBase']};                  // Base cost for Varak Baski (first 1250 units)\n"
        js_code += f"const VARAK_BASKI_PER_PIECE = {config['varakBaskiPerPiece']};             // Additional cost per piece for Varak Baski (beyond 1250 units)\n"
        js_code += f"const GOFRE_KLISE_BUYUK = {config['gofreKliseBuyuk']};                 // Cost for Buyuk Gofre Klise\n"
        js_code += f"const GOFRE_KLISE_UFAK = {config['gofreKliseUfak']};                  // Cost for Ufak Gofre Klise\n"
        js_code += f"const GOFRE_BASKI_BASE = {config['gofreBaskiBase']};                  // Base cost for Gofre Baski (first 1250 units)\n"
        js_code += f"const GOFRE_BASKI_PER_PIECE = {config['gofreBaskiPerPiece']};             // Additional cost per piece for Gofre Baski (beyond 1250 units)\n\n"
        js_code += "// Yapistirma per-piece costs (beyond base 1250 units)\n"
        js_code += f"const YAPISTIRMA_EKLEMELI_PER_PIECE = {config['yapistirmaEklemeliPerPiece']};     // Per piece cost for Eklemeli beyond base\n"
        js_code += f"const YAPISTIRMA_TEK_PARCA_PER_PIECE = {config['yapistirmaTekParcaPerPiece']};    // Per piece cost for Tek Parça beyond base\n"
        js_code += f"const YAPISTIRMA_PASTANE_PER_PIECE = {config['yapistirmaPastanePerPiece']};      // Per piece cost for Pastane beyond base\n\n"
        
        # Default GSM values
        js_code += "// Default GSM values\n"
        js_code += f"const KUTU_DEFAULT_GSM = {config['kutuDefaultGsm']};                   // Default GSM for boxes\n"
        js_code += f"const CANTA_DEFAULT_GSM = {config['cantaDefaultGsm']};                  // Default GSM for bags\n\n"
        
        # Paper size definitions
        js_code += "// Paper size definitions\n"
        js_code += "const PAPER_SIZES = [\n"
        
        # Add paper sizes from the configuration
        for paper in config['paperSizes']:
            js_code += f"  {{ name: '{paper['name']}', width: {paper['width']}, height: {paper['height']} }},\n"
        
        # Remove the last comma
        js_code = js_code.rstrip(',\n') + '\n'
        js_code += "];\n"
        
        # Write the JavaScript code to the file
        with open('static/js/pricing-config.js', 'w', encoding='utf-8') as f:
            f.write(js_code)
            
        return jsonify({'success': True})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
