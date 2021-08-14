from typing import Any, Dict, Iterable, Tuple
import numpy as np


class ASCIIGrid:
    N_HEADER_ROWS = 6
    CELL_SIZE_PRECISION = 6 # number of digits
    
    def __init__(self, filename: str):
        self.meta = self._read_metadata(filename)
        self.grid = self._read_grid(filename)

    @property
    def rows(self) -> int:
        return self.grid.shape[0]

    @property
    def cols(self) -> int:
        return self.grid.shape[1]

    @property
    def cell_size(self) -> float:
        return self.meta["cellsize"]

    @property
    def _nodata_value(self) -> int:
        return int(self.meta["NODATA_value"])

    @property
    def origin(self) -> Tuple[float, float]:
        return (self.meta["yllcorner"] + self.cell_size * (self.rows - 0.5),
                self.meta["xllcorner"] + self.cell_size * 0.5)

    def _read_metadata(self, filename: str) -> dict:
        meta = {}
        
        with open(filename, "r") as f:
            for _ in range(self.N_HEADER_ROWS):
                vals = f.readline().strip().split()
                meta[vals[0]] = self._meta_val(vals[1])
        
        # note: cell size gets weird due to floats
        meta["cellsize"] = round(meta["cellsize"], self.CELL_SIZE_PRECISION)

        return meta
    
    def _meta_val(self, raw: str) -> Any:
        if "." in raw:
            return float(raw)
        return int(raw)
    
    def _read_grid(self, filename: str) -> np.array:
        # read file and replace NO_DATA with np.nan
        grid = np.loadtxt(filename, skiprows=6)
        return np.where(grid == self._nodata_value, np.nan, grid)


class ASCIIGridJoin:
    def __init__(self, **grids):
        self.grids = grids
        self._validate_compatibility()
    
    @property
    def _first(self) -> ASCIIGrid:
        return self.grids[list(self.grids.keys())[0]]
    
    def _validate_compatibility(self) -> bool:
        for key in iter(self._first.meta.keys()):
            vals = set([grid.meta[key] for grid in iter(self.grids.values())])
            if len(vals) > 1:
                raise RuntimeError(f"Grids are not compatible for join: non-unique {key}")
        
        return True

    def entries(self) -> Iterable[Dict[str, Any]]:
        first = self._first
        for row in range(first.rows):
            for col in range(first.cols):
                data = {k: self.grids[k].grid[row, col] for k in self.grids.keys()}
                data["point"] = (first.origin[0] - first.cell_size * row, first.origin[1] + first.cell_size * col)
                yield data
