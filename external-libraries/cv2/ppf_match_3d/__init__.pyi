import cv2.typing
import typing


# Classes
class ICP:
    # Functions
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, iterations: int, tolerence: float = ..., rejectionScale: float = ..., numLevels: int = ..., sampleType: int = ..., numMaxCorr: int = ...) -> None: ...

    @typing.overload
    def registerModelToScene(self, srcPC: cv2.typing.MatLike, dstPC: cv2.typing.MatLike) -> tuple[int, float, cv2.typing.Matx44d]: ...
    @typing.overload
    def registerModelToScene(self, srcPC: cv2.typing.MatLike, dstPC: cv2.typing.MatLike, poses: typing.Sequence[Pose3D]) -> tuple[int, typing.Sequence[Pose3D]]: ...


class Pose3D:
    @property
    def alpha(self) -> float: ...
    @property
    def residual(self) -> float: ...
    @property
    def modelIndex(self) -> int: ...
    @property
    def numVotes(self) -> int: ...
    @property
    def pose(self) -> cv2.typing.Matx44d: ...
    @property
    def angle(self) -> float: ...
    @property
    def t(self) -> cv2.typing.Vec3d: ...
    @property
    def q(self) -> cv2.typing.Vec4d: ...

    # Functions
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, Alpha: float, ModelIndex: int = ..., NumVotes: int = ...) -> None: ...

    @typing.overload
    def updatePose(self, NewPose: cv2.typing.Matx44d) -> None: ...
    @typing.overload
    def updatePose(self, NewR: cv2.typing.Matx33d, NewT: cv2.typing.Vec3d) -> None: ...

    def updatePoseQuat(self, Q: cv2.typing.Vec4d, NewT: cv2.typing.Vec3d) -> None: ...

    def appendPose(self, IncrementalPose: cv2.typing.Matx44d) -> None: ...

    def printPose(self) -> None: ...


class PoseCluster3D:
    ...

class PPF3DDetector:
    # Functions
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, relativeSamplingStep: float, relativeDistanceStep: float = ..., numAngles: float = ...) -> None: ...

    def trainModel(self, Model: cv2.typing.MatLike) -> None: ...

    def match(self, scene: cv2.typing.MatLike, relativeSceneSampleStep: float = ..., relativeSceneDistance: float = ...) -> typing.Sequence[Pose3D]: ...



# Functions
def addNoisePC(pc: cv2.typing.MatLike, scale: float) -> cv2.typing.MatLike: ...

def computeNormalsPC3d(PC: cv2.typing.MatLike, NumNeighbors: int, FlipViewpoint: bool, viewpoint: cv2.typing.Vec3f, PCNormals: cv2.typing.MatLike | None = ...) -> tuple[int, cv2.typing.MatLike]: ...

def getRandomPose(Pose: cv2.typing.Matx44d) -> None: ...

def loadPLYSimple(fileName: str, withNormals: int = ...) -> cv2.typing.MatLike: ...

def samplePCByQuantization(pc: cv2.typing.MatLike, xrange: cv2.typing.Vec2f, yrange: cv2.typing.Vec2f, zrange: cv2.typing.Vec2f, sample_step_relative: float, weightByCenter: int = ...) -> cv2.typing.MatLike: ...

def transformPCPose(pc: cv2.typing.MatLike, Pose: cv2.typing.Matx44d) -> cv2.typing.MatLike: ...

def writePLY(PC: cv2.typing.MatLike, fileName: str) -> None: ...

def writePLYVisibleNormals(PC: cv2.typing.MatLike, fileName: str) -> None: ...

