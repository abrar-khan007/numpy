import re
import pathlib
from typing import IO, List

import numpy.typing as npt
import numpy as np

str_path: str
pathlib_path: pathlib.Path
str_file: IO[str]
bytes_file: IO[bytes]

bag_obj: np.lib.npyio.BagObj[int]
npz_file: np.lib.npyio.NpzFile

AR_i8: npt.NDArray[np.int64]
AR_LIKE_f8: List[float]

reveal_type(bag_obj.a)  # E: int
reveal_type(bag_obj.b)  # E: int

reveal_type(npz_file.zip)  # E: zipfile.ZipFile
reveal_type(npz_file.fid)  # E: Union[None, typing.IO[builtins.str]]
reveal_type(npz_file.files)  # E: list[builtins.str]
reveal_type(npz_file.allow_pickle)  # E: bool
reveal_type(npz_file.pickle_kwargs)  # E: Union[None, typing.Mapping[builtins.str, Any]]
reveal_type(npz_file.f)  # E: numpy.lib.npyio.BagObj[numpy.lib.npyio.NpzFile]
reveal_type(npz_file["test"])  # E: numpy.ndarray[Any, numpy.dtype[Any]]
reveal_type(len(npz_file))  # E: int
with npz_file as f:
    reveal_type(f)  # E: numpy.lib.npyio.NpzFile

reveal_type(np.load(bytes_file))  # E: Any
reveal_type(np.load(pathlib_path, allow_pickle=True))  # E: Any
reveal_type(np.load(str_path, encoding="bytes"))  # E: Any

reveal_type(np.save(bytes_file, AR_LIKE_f8))  # E: None
reveal_type(np.save(pathlib_path, AR_i8, allow_pickle=True))  # E: None
reveal_type(np.save(str_path, AR_LIKE_f8))  # E: None

reveal_type(np.savez(bytes_file, AR_LIKE_f8))  # E: None
reveal_type(np.savez(pathlib_path, ar1=AR_i8, ar2=AR_i8))  # E: None
reveal_type(np.savez(str_path, AR_LIKE_f8, ar1=AR_i8))  # E: None

reveal_type(np.savez_compressed(bytes_file, AR_LIKE_f8))  # E: None
reveal_type(np.savez_compressed(pathlib_path, ar1=AR_i8, ar2=AR_i8))  # E: None
reveal_type(np.savez_compressed(str_path, AR_LIKE_f8, ar1=AR_i8))  # E: None

reveal_type(np.loadtxt(bytes_file))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]
reveal_type(np.loadtxt(pathlib_path, dtype=np.str_))  # E: numpy.ndarray[Any, numpy.dtype[numpy.str_]]
reveal_type(np.loadtxt(str_path, dtype=str, skiprows=2))  # E: numpy.ndarray[Any, numpy.dtype[Any]]
reveal_type(np.loadtxt(str_file, comments="test"))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]
reveal_type(np.loadtxt(str_path, delimiter="\n"))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]
reveal_type(np.loadtxt(str_path, ndmin=2))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]

reveal_type(np.fromregex(bytes_file, "test", np.float64))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]
reveal_type(np.fromregex(str_file, b"test", dtype=float))  # E: numpy.ndarray[Any, numpy.dtype[Any]]
reveal_type(np.fromregex(str_path, re.compile("test"), dtype=np.str_, encoding="utf8"))  # E: numpy.ndarray[Any, numpy.dtype[numpy.str_]]
reveal_type(np.fromregex(pathlib_path, "test", np.float64))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]

reveal_type(np.genfromtxt(bytes_file))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]
reveal_type(np.genfromtxt(pathlib_path, dtype=np.str_))  # E: numpy.ndarray[Any, numpy.dtype[numpy.str_]]
reveal_type(np.genfromtxt(str_path, dtype=str, skiprows=2))  # E: numpy.ndarray[Any, numpy.dtype[Any]]
reveal_type(np.genfromtxt(str_file, comments="test"))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]
reveal_type(np.genfromtxt(str_path, delimiter="\n"))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]
reveal_type(np.genfromtxt(str_path, ndmin=2))  # E: numpy.ndarray[Any, numpy.dtype[{float64}]]

reveal_type(np.recfromtxt(bytes_file))  # E: numpy.recarray[Any, numpy.dtype[numpy.void]]
reveal_type(np.recfromtxt(pathlib_path, usemask=True))  # E: numpy.ma.mrecords.MaskedRecords[Any, numpy.dtype[numpy.void]]

reveal_type(np.recfromcsv(bytes_file))  # E: numpy.recarray[Any, numpy.dtype[numpy.void]]
reveal_type(np.recfromcsv(pathlib_path, usemask=True))  # E: numpy.ma.mrecords.MaskedRecords[Any, numpy.dtype[numpy.void]]
