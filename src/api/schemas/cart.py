from pydantic import BaseModel, ConfigDict

class Product(BaseModel):
	model_config = ConfigDict(extra="forbid")

	id: int
	title: str
	price: float
	quantity: int
	total: float
	discountPercentage: float
	discountedPrice: float
	thumbnail: str

class Cart(BaseModel):
	model_config = ConfigDict(extra="forbid")

	id: int
	products: list[Product]
	total: float
	discountedTotal: float
	userId: int
	totalProducts: int
	totalQuantity: int

class ProductDetail(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    title: str
    price: float
    quantity: int
    total: float
    discountPercentage: float
    discountedTotal: float
    thumbnail: str

class CartDetail(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    products: list[ProductDetail]
    total: float
    discountedTotal: float
    userId: int
    totalProducts: int
    totalQuantity: int

class DeletedCart(CartDetail):
    model_config = ConfigDict(extra="forbid")

    isDeleted: bool
    deletedOn: str
