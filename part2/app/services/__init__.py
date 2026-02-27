# app/services/__init__.py

from .facade import HBnBFacade

# On crée une seule instance (un Singleton) de la Façade.
# C'est cet objet précis que TOUTE ton application va utiliser.
facade = HBnBFacade()
