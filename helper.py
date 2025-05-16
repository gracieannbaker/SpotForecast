import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin


class ResidualBoostClassifier(BaseEstimator, RegressorMixin):
    def __init__(self, base_reg=None, residual_reg=None, threshold=0.5):
        self.base_reg = base_reg
        self.residual_reg = residual_reg
        self.threshhold = threshold

    def fit(self, X, y):
        # Fit base regressor
        self.base_reg.fit(X, y)

        # Compute Residuals
        residuals = y - self.base_reg.predict(X)
        # Fit the second regressor with the residuals?
        self.residual_reg.fit(X, residuals)
        return self
    

    def predict(self, X):
        # main prediction plus correction
        main_pred = self.base_reg.predict(X)
        corr      = self.residual_reg.predict(X)
        return main_pred + corr


