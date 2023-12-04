import cv2
import cv2.typing
import typing


# Enumerations
VAR_NUMERICAL: int
VAR_ORDERED: int
VAR_CATEGORICAL: int
VariableTypes = int
"""One of [VAR_NUMERICAL, VAR_ORDERED, VAR_CATEGORICAL]"""

TEST_ERROR: int
TRAIN_ERROR: int
ErrorTypes = int
"""One of [TEST_ERROR, TRAIN_ERROR]"""

ROW_SAMPLE: int
COL_SAMPLE: int
SampleTypes = int
"""One of [ROW_SAMPLE, COL_SAMPLE]"""


StatModel_UPDATE_MODEL: int
STAT_MODEL_UPDATE_MODEL: int
StatModel_RAW_OUTPUT: int
STAT_MODEL_RAW_OUTPUT: int
StatModel_COMPRESSED_INPUT: int
STAT_MODEL_COMPRESSED_INPUT: int
StatModel_PREPROCESSED_INPUT: int
STAT_MODEL_PREPROCESSED_INPUT: int
StatModel_Flags = int
"""One of [StatModel_UPDATE_MODEL, STAT_MODEL_UPDATE_MODEL, StatModel_RAW_OUTPUT, STAT_MODEL_RAW_OUTPUT, StatModel_COMPRESSED_INPUT, STAT_MODEL_COMPRESSED_INPUT, StatModel_PREPROCESSED_INPUT, STAT_MODEL_PREPROCESSED_INPUT]"""

KNearest_BRUTE_FORCE: int
KNEAREST_BRUTE_FORCE: int
KNearest_KDTREE: int
KNEAREST_KDTREE: int
KNearest_Types = int
"""One of [KNearest_BRUTE_FORCE, KNEAREST_BRUTE_FORCE, KNearest_KDTREE, KNEAREST_KDTREE]"""

SVM_C_SVC: int
SVM_NU_SVC: int
SVM_ONE_CLASS: int
SVM_EPS_SVR: int
SVM_NU_SVR: int
SVM_Types = int
"""One of [SVM_C_SVC, SVM_NU_SVC, SVM_ONE_CLASS, SVM_EPS_SVR, SVM_NU_SVR]"""

SVM_CUSTOM: int
SVM_LINEAR: int
SVM_POLY: int
SVM_RBF: int
SVM_SIGMOID: int
SVM_CHI2: int
SVM_INTER: int
SVM_KernelTypes = int
"""One of [SVM_CUSTOM, SVM_LINEAR, SVM_POLY, SVM_RBF, SVM_SIGMOID, SVM_CHI2, SVM_INTER]"""

SVM_C: int
SVM_GAMMA: int
SVM_P: int
SVM_NU: int
SVM_COEF: int
SVM_DEGREE: int
SVM_ParamTypes = int
"""One of [SVM_C, SVM_GAMMA, SVM_P, SVM_NU, SVM_COEF, SVM_DEGREE]"""

EM_COV_MAT_SPHERICAL: int
EM_COV_MAT_DIAGONAL: int
EM_COV_MAT_GENERIC: int
EM_COV_MAT_DEFAULT: int
EM_Types = int
"""One of [EM_COV_MAT_SPHERICAL, EM_COV_MAT_DIAGONAL, EM_COV_MAT_GENERIC, EM_COV_MAT_DEFAULT]"""

EM_DEFAULT_NCLUSTERS: int
EM_DEFAULT_MAX_ITERS: int
EM_START_E_STEP: int
EM_START_M_STEP: int
EM_START_AUTO_STEP: int

DTrees_PREDICT_AUTO: int
DTREES_PREDICT_AUTO: int
DTrees_PREDICT_SUM: int
DTREES_PREDICT_SUM: int
DTrees_PREDICT_MAX_VOTE: int
DTREES_PREDICT_MAX_VOTE: int
DTrees_PREDICT_MASK: int
DTREES_PREDICT_MASK: int
DTrees_Flags = int
"""One of [DTrees_PREDICT_AUTO, DTREES_PREDICT_AUTO, DTrees_PREDICT_SUM, DTREES_PREDICT_SUM, DTrees_PREDICT_MAX_VOTE, DTREES_PREDICT_MAX_VOTE, DTrees_PREDICT_MASK, DTREES_PREDICT_MASK]"""

Boost_DISCRETE: int
BOOST_DISCRETE: int
Boost_REAL: int
BOOST_REAL: int
Boost_LOGIT: int
BOOST_LOGIT: int
Boost_GENTLE: int
BOOST_GENTLE: int
Boost_Types = int
"""One of [Boost_DISCRETE, BOOST_DISCRETE, Boost_REAL, BOOST_REAL, Boost_LOGIT, BOOST_LOGIT, Boost_GENTLE, BOOST_GENTLE]"""

ANN_MLP_BACKPROP: int
ANN_MLP_RPROP: int
ANN_MLP_ANNEAL: int
ANN_MLP_TrainingMethods = int
"""One of [ANN_MLP_BACKPROP, ANN_MLP_RPROP, ANN_MLP_ANNEAL]"""

ANN_MLP_IDENTITY: int
ANN_MLP_SIGMOID_SYM: int
ANN_MLP_GAUSSIAN: int
ANN_MLP_RELU: int
ANN_MLP_LEAKYRELU: int
ANN_MLP_ActivationFunctions = int
"""One of [ANN_MLP_IDENTITY, ANN_MLP_SIGMOID_SYM, ANN_MLP_GAUSSIAN, ANN_MLP_RELU, ANN_MLP_LEAKYRELU]"""

ANN_MLP_UPDATE_WEIGHTS: int
ANN_MLP_NO_INPUT_SCALE: int
ANN_MLP_NO_OUTPUT_SCALE: int
ANN_MLP_TrainFlags = int
"""One of [ANN_MLP_UPDATE_WEIGHTS, ANN_MLP_NO_INPUT_SCALE, ANN_MLP_NO_OUTPUT_SCALE]"""

LogisticRegression_REG_DISABLE: int
LOGISTIC_REGRESSION_REG_DISABLE: int
LogisticRegression_REG_L1: int
LOGISTIC_REGRESSION_REG_L1: int
LogisticRegression_REG_L2: int
LOGISTIC_REGRESSION_REG_L2: int
LogisticRegression_RegKinds = int
"""One of [LogisticRegression_REG_DISABLE, LOGISTIC_REGRESSION_REG_DISABLE, LogisticRegression_REG_L1, LOGISTIC_REGRESSION_REG_L1, LogisticRegression_REG_L2, LOGISTIC_REGRESSION_REG_L2]"""

LogisticRegression_BATCH: int
LOGISTIC_REGRESSION_BATCH: int
LogisticRegression_MINI_BATCH: int
LOGISTIC_REGRESSION_MINI_BATCH: int
LogisticRegression_Methods = int
"""One of [LogisticRegression_BATCH, LOGISTIC_REGRESSION_BATCH, LogisticRegression_MINI_BATCH, LOGISTIC_REGRESSION_MINI_BATCH]"""

SVMSGD_SGD: int
SVMSGD_ASGD: int
SVMSGD_SvmsgdType = int
"""One of [SVMSGD_SGD, SVMSGD_ASGD]"""

SVMSGD_SOFT_MARGIN: int
SVMSGD_HARD_MARGIN: int
SVMSGD_MarginType = int
"""One of [SVMSGD_SOFT_MARGIN, SVMSGD_HARD_MARGIN]"""


# Classes
class ParamGrid:
    minVal: float
    maxVal: float
    logStep: float

    # Functions
    @classmethod
    def create(cls, minVal: float = ..., maxVal: float = ..., logstep: float = ...) -> ParamGrid: ...


class TrainData:
    # Functions
    def getLayout(self) -> int: ...

    def getNTrainSamples(self) -> int: ...

    def getNTestSamples(self) -> int: ...

    def getNSamples(self) -> int: ...

    def getNVars(self) -> int: ...

    def getNAllVars(self) -> int: ...

    @typing.overload
    def getSample(self, varIdx: cv2.typing.MatLike, sidx: int, buf: float) -> None: ...
    @typing.overload
    def getSample(self, varIdx: cv2.UMat, sidx: int, buf: float) -> None: ...

    def getSamples(self) -> cv2.typing.MatLike: ...

    def getMissing(self) -> cv2.typing.MatLike: ...

    def getTrainSamples(self, layout: int = ..., compressSamples: bool = ..., compressVars: bool = ...) -> cv2.typing.MatLike: ...

    def getTrainResponses(self) -> cv2.typing.MatLike: ...

    def getTrainNormCatResponses(self) -> cv2.typing.MatLike: ...

    def getTestResponses(self) -> cv2.typing.MatLike: ...

    def getTestNormCatResponses(self) -> cv2.typing.MatLike: ...

    def getResponses(self) -> cv2.typing.MatLike: ...

    def getNormCatResponses(self) -> cv2.typing.MatLike: ...

    def getSampleWeights(self) -> cv2.typing.MatLike: ...

    def getTrainSampleWeights(self) -> cv2.typing.MatLike: ...

    def getTestSampleWeights(self) -> cv2.typing.MatLike: ...

    def getVarIdx(self) -> cv2.typing.MatLike: ...

    def getVarType(self) -> cv2.typing.MatLike: ...

    def getVarSymbolFlags(self) -> cv2.typing.MatLike: ...

    def getResponseType(self) -> int: ...

    def getTrainSampleIdx(self) -> cv2.typing.MatLike: ...

    def getTestSampleIdx(self) -> cv2.typing.MatLike: ...

    @typing.overload
    def getValues(self, vi: int, sidx: cv2.typing.MatLike, values: float) -> None: ...
    @typing.overload
    def getValues(self, vi: int, sidx: cv2.UMat, values: float) -> None: ...

    def getDefaultSubstValues(self) -> cv2.typing.MatLike: ...

    def getCatCount(self, vi: int) -> int: ...

    def getClassLabels(self) -> cv2.typing.MatLike: ...

    def getCatOfs(self) -> cv2.typing.MatLike: ...

    def getCatMap(self) -> cv2.typing.MatLike: ...

    def setTrainTestSplit(self, count: int, shuffle: bool = ...) -> None: ...

    def setTrainTestSplitRatio(self, ratio: float, shuffle: bool = ...) -> None: ...

    def shuffleTrainTest(self) -> None: ...

    def getTestSamples(self) -> cv2.typing.MatLike: ...

    def getNames(self, names: typing.Sequence[str]) -> None: ...

    @staticmethod
    def getSubVector(vec: cv2.typing.MatLike, idx: cv2.typing.MatLike) -> cv2.typing.MatLike: ...

    @staticmethod
    def getSubMatrix(matrix: cv2.typing.MatLike, idx: cv2.typing.MatLike, layout: int) -> cv2.typing.MatLike: ...

    @classmethod
    @typing.overload
    def create(cls, samples: cv2.typing.MatLike, layout: int, responses: cv2.typing.MatLike, varIdx: cv2.typing.MatLike | None = ..., sampleIdx: cv2.typing.MatLike | None = ..., sampleWeights: cv2.typing.MatLike | None = ..., varType: cv2.typing.MatLike | None = ...) -> TrainData: ...
    @classmethod
    @typing.overload
    def create(cls, samples: cv2.UMat, layout: int, responses: cv2.UMat, varIdx: cv2.UMat | None = ..., sampleIdx: cv2.UMat | None = ..., sampleWeights: cv2.UMat | None = ..., varType: cv2.UMat | None = ...) -> TrainData: ...


class StatModel(cv2.Algorithm):
    # Functions
    def getVarCount(self) -> int: ...

    def empty(self) -> bool: ...

    def isTrained(self) -> bool: ...

    def isClassifier(self) -> bool: ...

    @typing.overload
    def train(self, trainData: TrainData, flags: int = ...) -> bool: ...
    @typing.overload
    def train(self, samples: cv2.typing.MatLike, layout: int, responses: cv2.typing.MatLike) -> bool: ...
    @typing.overload
    def train(self, samples: cv2.UMat, layout: int, responses: cv2.UMat) -> bool: ...

    @typing.overload
    def calcError(self, data: TrainData, test: bool, resp: cv2.typing.MatLike | None = ...) -> tuple[float, cv2.typing.MatLike]: ...
    @typing.overload
    def calcError(self, data: TrainData, test: bool, resp: cv2.UMat | None = ...) -> tuple[float, cv2.UMat]: ...

    @typing.overload
    def predict(self, samples: cv2.typing.MatLike, results: cv2.typing.MatLike | None = ..., flags: int = ...) -> tuple[float, cv2.typing.MatLike]: ...
    @typing.overload
    def predict(self, samples: cv2.UMat, results: cv2.UMat | None = ..., flags: int = ...) -> tuple[float, cv2.UMat]: ...


class NormalBayesClassifier(StatModel):
    # Functions
    @typing.overload
    def predictProb(self, inputs: cv2.typing.MatLike, outputs: cv2.typing.MatLike | None = ..., outputProbs: cv2.typing.MatLike | None = ..., flags: int = ...) -> tuple[float, cv2.typing.MatLike, cv2.typing.MatLike]: ...
    @typing.overload
    def predictProb(self, inputs: cv2.UMat, outputs: cv2.UMat | None = ..., outputProbs: cv2.UMat | None = ..., flags: int = ...) -> tuple[float, cv2.UMat, cv2.UMat]: ...

    @classmethod
    def create(cls) -> NormalBayesClassifier: ...

    @classmethod
    def load(cls, filepath: str, nodeName: str = ...) -> NormalBayesClassifier: ...


class KNearest(StatModel):
    # Functions
    def getDefaultK(self) -> int: ...

    def setDefaultK(self, val: int) -> None: ...

    def getIsClassifier(self) -> bool: ...

    def setIsClassifier(self, val: bool) -> None: ...

    def getEmax(self) -> int: ...

    def setEmax(self, val: int) -> None: ...

    def getAlgorithmType(self) -> int: ...

    def setAlgorithmType(self, val: int) -> None: ...

    @typing.overload
    def findNearest(self, samples: cv2.typing.MatLike, k: int, results: cv2.typing.MatLike | None = ..., neighborResponses: cv2.typing.MatLike | None = ..., dist: cv2.typing.MatLike | None = ...) -> tuple[float, cv2.typing.MatLike, cv2.typing.MatLike, cv2.typing.MatLike]: ...
    @typing.overload
    def findNearest(self, samples: cv2.UMat, k: int, results: cv2.UMat | None = ..., neighborResponses: cv2.UMat | None = ..., dist: cv2.UMat | None = ...) -> tuple[float, cv2.UMat, cv2.UMat, cv2.UMat]: ...

    @classmethod
    def create(cls) -> KNearest: ...

    @classmethod
    def load(cls, filepath: str) -> KNearest: ...


class SVM(StatModel):
    # Functions
    def getType(self) -> int: ...

    def setType(self, val: int) -> None: ...

    def getGamma(self) -> float: ...

    def setGamma(self, val: float) -> None: ...

    def getCoef0(self) -> float: ...

    def setCoef0(self, val: float) -> None: ...

    def getDegree(self) -> float: ...

    def setDegree(self, val: float) -> None: ...

    def getC(self) -> float: ...

    def setC(self, val: float) -> None: ...

    def getNu(self) -> float: ...

    def setNu(self, val: float) -> None: ...

    def getP(self) -> float: ...

    def setP(self, val: float) -> None: ...

    def getClassWeights(self) -> cv2.typing.MatLike: ...

    def setClassWeights(self, val: cv2.typing.MatLike) -> None: ...

    def getTermCriteria(self) -> cv2.typing.TermCriteria: ...

    def setTermCriteria(self, val: cv2.typing.TermCriteria) -> None: ...

    def getKernelType(self) -> int: ...

    def setKernel(self, kernelType: int) -> None: ...

    @typing.overload
    def trainAuto(self, samples: cv2.typing.MatLike, layout: int, responses: cv2.typing.MatLike, kFold: int = ..., Cgrid: ParamGrid = ..., gammaGrid: ParamGrid = ..., pGrid: ParamGrid = ..., nuGrid: ParamGrid = ..., coeffGrid: ParamGrid = ..., degreeGrid: ParamGrid = ..., balanced: bool = ...) -> bool: ...
    @typing.overload
    def trainAuto(self, samples: cv2.UMat, layout: int, responses: cv2.UMat, kFold: int = ..., Cgrid: ParamGrid = ..., gammaGrid: ParamGrid = ..., pGrid: ParamGrid = ..., nuGrid: ParamGrid = ..., coeffGrid: ParamGrid = ..., degreeGrid: ParamGrid = ..., balanced: bool = ...) -> bool: ...

    def getSupportVectors(self) -> cv2.typing.MatLike: ...

    def getUncompressedSupportVectors(self) -> cv2.typing.MatLike: ...

    @typing.overload
    def getDecisionFunction(self, i: int, alpha: cv2.typing.MatLike | None = ..., svidx: cv2.typing.MatLike | None = ...) -> tuple[float, cv2.typing.MatLike, cv2.typing.MatLike]: ...
    @typing.overload
    def getDecisionFunction(self, i: int, alpha: cv2.UMat | None = ..., svidx: cv2.UMat | None = ...) -> tuple[float, cv2.UMat, cv2.UMat]: ...

    @staticmethod
    def getDefaultGridPtr(param_id: int) -> ParamGrid: ...

    @classmethod
    def create(cls) -> SVM: ...

    @classmethod
    def load(cls, filepath: str) -> SVM: ...


class EM(StatModel):
    # Functions
    def getClustersNumber(self) -> int: ...

    def setClustersNumber(self, val: int) -> None: ...

    def getCovarianceMatrixType(self) -> int: ...

    def setCovarianceMatrixType(self, val: int) -> None: ...

    def getTermCriteria(self) -> cv2.typing.TermCriteria: ...

    def setTermCriteria(self, val: cv2.typing.TermCriteria) -> None: ...

    def getWeights(self) -> cv2.typing.MatLike: ...

    def getMeans(self) -> cv2.typing.MatLike: ...

    def getCovs(self, covs: typing.Sequence[cv2.typing.MatLike] | None = ...) -> typing.Sequence[cv2.typing.MatLike]: ...

    @typing.overload
    def predict(self, samples: cv2.typing.MatLike, results: cv2.typing.MatLike | None = ..., flags: int = ...) -> tuple[float, cv2.typing.MatLike]: ...
    @typing.overload
    def predict(self, samples: cv2.UMat, results: cv2.UMat | None = ..., flags: int = ...) -> tuple[float, cv2.UMat]: ...

    @typing.overload
    def predict2(self, sample: cv2.typing.MatLike, probs: cv2.typing.MatLike | None = ...) -> tuple[cv2.typing.Vec2d, cv2.typing.MatLike]: ...
    @typing.overload
    def predict2(self, sample: cv2.UMat, probs: cv2.UMat | None = ...) -> tuple[cv2.typing.Vec2d, cv2.UMat]: ...

    @typing.overload
    def trainEM(self, samples: cv2.typing.MatLike, logLikelihoods: cv2.typing.MatLike | None = ..., labels: cv2.typing.MatLike | None = ..., probs: cv2.typing.MatLike | None = ...) -> tuple[bool, cv2.typing.MatLike, cv2.typing.MatLike, cv2.typing.MatLike]: ...
    @typing.overload
    def trainEM(self, samples: cv2.UMat, logLikelihoods: cv2.UMat | None = ..., labels: cv2.UMat | None = ..., probs: cv2.UMat | None = ...) -> tuple[bool, cv2.UMat, cv2.UMat, cv2.UMat]: ...

    @typing.overload
    def trainE(self, samples: cv2.typing.MatLike, means0: cv2.typing.MatLike, covs0: cv2.typing.MatLike | None = ..., weights0: cv2.typing.MatLike | None = ..., logLikelihoods: cv2.typing.MatLike | None = ..., labels: cv2.typing.MatLike | None = ..., probs: cv2.typing.MatLike | None = ...) -> tuple[bool, cv2.typing.MatLike, cv2.typing.MatLike, cv2.typing.MatLike]: ...
    @typing.overload
    def trainE(self, samples: cv2.UMat, means0: cv2.UMat, covs0: cv2.UMat | None = ..., weights0: cv2.UMat | None = ..., logLikelihoods: cv2.UMat | None = ..., labels: cv2.UMat | None = ..., probs: cv2.UMat | None = ...) -> tuple[bool, cv2.UMat, cv2.UMat, cv2.UMat]: ...

    @typing.overload
    def trainM(self, samples: cv2.typing.MatLike, probs0: cv2.typing.MatLike, logLikelihoods: cv2.typing.MatLike | None = ..., labels: cv2.typing.MatLike | None = ..., probs: cv2.typing.MatLike | None = ...) -> tuple[bool, cv2.typing.MatLike, cv2.typing.MatLike, cv2.typing.MatLike]: ...
    @typing.overload
    def trainM(self, samples: cv2.UMat, probs0: cv2.UMat, logLikelihoods: cv2.UMat | None = ..., labels: cv2.UMat | None = ..., probs: cv2.UMat | None = ...) -> tuple[bool, cv2.UMat, cv2.UMat, cv2.UMat]: ...

    @classmethod
    def create(cls) -> EM: ...

    @classmethod
    def load(cls, filepath: str, nodeName: str = ...) -> EM: ...


class DTrees(StatModel):
    # Functions
    def getMaxCategories(self) -> int: ...

    def setMaxCategories(self, val: int) -> None: ...

    def getMaxDepth(self) -> int: ...

    def setMaxDepth(self, val: int) -> None: ...

    def getMinSampleCount(self) -> int: ...

    def setMinSampleCount(self, val: int) -> None: ...

    def getCVFolds(self) -> int: ...

    def setCVFolds(self, val: int) -> None: ...

    def getUseSurrogates(self) -> bool: ...

    def setUseSurrogates(self, val: bool) -> None: ...

    def getUse1SERule(self) -> bool: ...

    def setUse1SERule(self, val: bool) -> None: ...

    def getTruncatePrunedTree(self) -> bool: ...

    def setTruncatePrunedTree(self, val: bool) -> None: ...

    def getRegressionAccuracy(self) -> float: ...

    def setRegressionAccuracy(self, val: float) -> None: ...

    def getPriors(self) -> cv2.typing.MatLike: ...

    def setPriors(self, val: cv2.typing.MatLike) -> None: ...

    @classmethod
    def create(cls) -> DTrees: ...

    @classmethod
    def load(cls, filepath: str, nodeName: str = ...) -> DTrees: ...


class ANN_MLP(StatModel):
    # Functions
    def setTrainMethod(self, method: int, param1: float = ..., param2: float = ...) -> None: ...

    def getTrainMethod(self) -> int: ...

    def setActivationFunction(self, type: int, param1: float = ..., param2: float = ...) -> None: ...

    @typing.overload
    def setLayerSizes(self, _layer_sizes: cv2.typing.MatLike) -> None: ...
    @typing.overload
    def setLayerSizes(self, _layer_sizes: cv2.UMat) -> None: ...

    def getLayerSizes(self) -> cv2.typing.MatLike: ...

    def getTermCriteria(self) -> cv2.typing.TermCriteria: ...

    def setTermCriteria(self, val: cv2.typing.TermCriteria) -> None: ...

    def getBackpropWeightScale(self) -> float: ...

    def setBackpropWeightScale(self, val: float) -> None: ...

    def getBackpropMomentumScale(self) -> float: ...

    def setBackpropMomentumScale(self, val: float) -> None: ...

    def getRpropDW0(self) -> float: ...

    def setRpropDW0(self, val: float) -> None: ...

    def getRpropDWPlus(self) -> float: ...

    def setRpropDWPlus(self, val: float) -> None: ...

    def getRpropDWMinus(self) -> float: ...

    def setRpropDWMinus(self, val: float) -> None: ...

    def getRpropDWMin(self) -> float: ...

    def setRpropDWMin(self, val: float) -> None: ...

    def getRpropDWMax(self) -> float: ...

    def setRpropDWMax(self, val: float) -> None: ...

    def getAnnealInitialT(self) -> float: ...

    def setAnnealInitialT(self, val: float) -> None: ...

    def getAnnealFinalT(self) -> float: ...

    def setAnnealFinalT(self, val: float) -> None: ...

    def getAnnealCoolingRatio(self) -> float: ...

    def setAnnealCoolingRatio(self, val: float) -> None: ...

    def getAnnealItePerStep(self) -> int: ...

    def setAnnealItePerStep(self, val: int) -> None: ...

    def getWeights(self, layerIdx: int) -> cv2.typing.MatLike: ...

    @classmethod
    def create(cls) -> ANN_MLP: ...

    @classmethod
    def load(cls, filepath: str) -> ANN_MLP: ...


class LogisticRegression(StatModel):
    # Functions
    def getLearningRate(self) -> float: ...

    def setLearningRate(self, val: float) -> None: ...

    def getIterations(self) -> int: ...

    def setIterations(self, val: int) -> None: ...

    def getRegularization(self) -> int: ...

    def setRegularization(self, val: int) -> None: ...

    def getTrainMethod(self) -> int: ...

    def setTrainMethod(self, val: int) -> None: ...

    def getMiniBatchSize(self) -> int: ...

    def setMiniBatchSize(self, val: int) -> None: ...

    def getTermCriteria(self) -> cv2.typing.TermCriteria: ...

    def setTermCriteria(self, val: cv2.typing.TermCriteria) -> None: ...

    @typing.overload
    def predict(self, samples: cv2.typing.MatLike, results: cv2.typing.MatLike | None = ..., flags: int = ...) -> tuple[float, cv2.typing.MatLike]: ...
    @typing.overload
    def predict(self, samples: cv2.UMat, results: cv2.UMat | None = ..., flags: int = ...) -> tuple[float, cv2.UMat]: ...

    def get_learnt_thetas(self) -> cv2.typing.MatLike: ...

    @classmethod
    def create(cls) -> LogisticRegression: ...

    @classmethod
    def load(cls, filepath: str, nodeName: str = ...) -> LogisticRegression: ...


class SVMSGD(StatModel):
    # Functions
    def getWeights(self) -> cv2.typing.MatLike: ...

    def getShift(self) -> float: ...

    @classmethod
    def create(cls) -> SVMSGD: ...

    @classmethod
    def load(cls, filepath: str, nodeName: str = ...) -> SVMSGD: ...

    def setOptimalParameters(self, svmsgdType: int = ..., marginType: int = ...) -> None: ...

    def getSvmsgdType(self) -> int: ...

    def setSvmsgdType(self, svmsgdType: int) -> None: ...

    def getMarginType(self) -> int: ...

    def setMarginType(self, marginType: int) -> None: ...

    def getMarginRegularization(self) -> float: ...

    def setMarginRegularization(self, marginRegularization: float) -> None: ...

    def getInitialStepSize(self) -> float: ...

    def setInitialStepSize(self, InitialStepSize: float) -> None: ...

    def getStepDecreasingPower(self) -> float: ...

    def setStepDecreasingPower(self, stepDecreasingPower: float) -> None: ...

    def getTermCriteria(self) -> cv2.typing.TermCriteria: ...

    def setTermCriteria(self, val: cv2.typing.TermCriteria) -> None: ...


class RTrees(DTrees):
    # Functions
    def getCalculateVarImportance(self) -> bool: ...

    def setCalculateVarImportance(self, val: bool) -> None: ...

    def getActiveVarCount(self) -> int: ...

    def setActiveVarCount(self, val: int) -> None: ...

    def getTermCriteria(self) -> cv2.typing.TermCriteria: ...

    def setTermCriteria(self, val: cv2.typing.TermCriteria) -> None: ...

    def getVarImportance(self) -> cv2.typing.MatLike: ...

    @typing.overload
    def getVotes(self, samples: cv2.typing.MatLike, flags: int, results: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def getVotes(self, samples: cv2.UMat, flags: int, results: cv2.UMat | None = ...) -> cv2.UMat: ...

    def getOOBError(self) -> float: ...

    @classmethod
    def create(cls) -> RTrees: ...

    @classmethod
    def load(cls, filepath: str, nodeName: str = ...) -> RTrees: ...


class Boost(DTrees):
    # Functions
    def getBoostType(self) -> int: ...

    def setBoostType(self, val: int) -> None: ...

    def getWeakCount(self) -> int: ...

    def setWeakCount(self, val: int) -> None: ...

    def getWeightTrimRate(self) -> float: ...

    def setWeightTrimRate(self, val: float) -> None: ...

    @classmethod
    def create(cls) -> Boost: ...

    @classmethod
    def load(cls, filepath: str, nodeName: str = ...) -> Boost: ...


