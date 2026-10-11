import numpy as np

def validate_numeric_data(data: np.ndarray) -> np.ndarray:
    """
    Valida um conjunto de dados numéricos.

    Args:
        data: Array NumPy contendo os dados.

    Returns:
        O array validado.

    Raises:
        TypeError: Se os dados não forem um array NumPy.
        ValueError: Se os dados estiverem vazios ou contiverem
            valores não finitos.
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Os dados devem ser um array NumPy.")

    if data.size == 0:
        raise ValueError("Os dados não podem estar vazios.")

    if not np.issubdtype(data.dtype, np.number):
        raise ValueError("Os dados devem conter valores numéricos.")

    if not np.isfinite(data).all():
        raise ValueError(
            "Os dados não podem conter NaN ou valores infinitos."
        )

    return data