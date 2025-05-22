from app import db
from datetime import datetime


class Customer(db.Model):
    """Customer information model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(150))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    quotations = db.relationship('Quotation', backref='customer', lazy=True)
    
    def __repr__(self):
        return f'<Customer {self.name}>'


class Quotation(db.Model):
    """Quotation model to store calculation results"""
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_type = db.Column(db.String(50))  # 'Kutu' or 'Çanta'
    product_info = db.Column(db.String(200))  # Additional product description
    quantity = db.Column(db.Integer, nullable=False)
    
    # Main sheet details
    width = db.Column(db.Float, nullable=False)  # Product width in cm
    height = db.Column(db.Float, nullable=False)  # Product height in cm
    paper_gsm = db.Column(db.Integer, nullable=False)  # Paper GSM
    paper_size = db.Column(db.String(20), nullable=False)  # e.g. "70x100"
    pieces_per_sheet = db.Column(db.Integer, nullable=False)
    
    # Options for main sheet
    selefon = db.Column(db.String(10))  # 'VAR' or 'YOK'
    lak = db.Column(db.String(10))  # 'VAR' or 'YOK'
    varak_klise = db.Column(db.String(10))  # 'Büyük', 'Ufak', or 'YOK'
    varak_baski = db.Column(db.String(10))  # 'VAR' or 'YOK'
    gofre_klise = db.Column(db.String(10))  # 'Büyük', 'Ufak', or 'YOK'
    gofre_baski = db.Column(db.String(10))  # 'VAR' or 'YOK'
    
    # Second sheet details
    has_second_sheet = db.Column(db.Boolean, default=False)
    second_width = db.Column(db.Float)  # Second sheet width in cm
    second_height = db.Column(db.Float)  # Second sheet height in cm
    second_paper_gsm = db.Column(db.Integer)  # Second sheet paper GSM
    second_paper_size = db.Column(db.String(20))  # e.g. "70x100"
    second_pieces_per_sheet = db.Column(db.Integer)
    
    # Options for second sheet
    second_selefon = db.Column(db.String(10))  # 'VAR' or 'YOK'
    second_bicak = db.Column(db.String(10))  # 'VAR' or 'YOK'
    second_kesim = db.Column(db.String(10))  # 'VAR' or 'YOK'
    
    # Cost details
    usd_to_tl = db.Column(db.Float, nullable=False)  # Exchange rate
    ambalaj = db.Column(db.Float, default=0)  # Packaging cost
    nakliye = db.Column(db.Float, default=0)  # Shipping cost
    vergi = db.Column(db.Float, default=0)  # Tax
    extra = db.Column(db.Float, default=0)  # Extra costs
    profit_margin = db.Column(db.Float, default=0)  # Profit margin percentage
    
    # Bag specific fields
    yapistirma_type = db.Column(db.String(20))  # 'Normal' or 'Silikonlu'
    yapistirma_sekli = db.Column(db.String(20))  # 'Eklemeli', 'Tek Parça', or 'Pastane'
    ip_turu = db.Column(db.String(20))  # 'Normal', 'Burgulu', or 'Saten'
    
    # Results
    total_cost = db.Column(db.Float, nullable=False)  # Total production cost
    second_sheet_cost = db.Column(db.Float)  # Second sheet cost if present
    selling_price = db.Column(db.Float, nullable=False)  # Final selling price
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Quotation {self.id} - {self.product_type}>'