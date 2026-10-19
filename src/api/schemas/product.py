from pydantic import BaseModel, ConfigDict

class DimensionsDetail(BaseModel):
    model_config = ConfigDict(extra="forbid")

    width: float
    height: float
    depth: float

class ReviewsDetail(BaseModel):
    model_config = ConfigDict(extra="forbid")

    rating: int
    comment: str
    date: str
    reviewerName: str
    reviewerEmail: str

class MetaDetail(BaseModel):
    model_config = ConfigDict(extra="forbid")

    createdAt: str
    updatedAt: str
    barcode: str
    qrCode: str

class ProductDetail(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: float
    rating: float
    stock: float
    tags: list[str]
    brand: str
    sku: str
    weight: float
    dimensions: DimensionsDetail
    warrantyInformation: str
    shippingInformation: str
    availabilityStatus: str
    reviews: list[ReviewsDetail]
    returnPolicy: str
    minimumOrderQuantity: int
    meta: MetaDetail
    images: list[str]
    thumbnail: str

class ProductSearch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    products: list[ProductDetail]
    total: int
    skip: int
    limit: int

class ProductUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    title: str
    price: float
    discountPercentage: float
    stock: int
    rating: float
    images: list[str]
    thumbnail: str
    description: str
    category: str