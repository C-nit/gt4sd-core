"""Graph MCTS implementation."""

import os

from guacamol_baselines.graph_mcts import goal_directed_generation
from guacamol_baselines.graph_mcts.goal_directed_generation import GB_MCTS_Generator


class GraphMCTS:
    def __init__(
        self,
        init_smiles: str,
        population_size: int,
        n_jobs: int,
        generations: int,
        patience: int,
        num_sims: float,
        max_children: int,
        max_atoms: int,
        pickle_directory: str = os.path.dirname(
            os.path.realpath(goal_directed_generation.__file__)
        ),
    ):
        """Initialize SMILESGA.

        Args:
            init_smiles: path where to load hypothesis, candidate labels and, optionally, the smiles file.
            population_size: used with n_mutations for the initial generation of smiles within the population
            n_jobs: number of concurrently running jobs
            generations: number of evolutionary generations
            patience: used for early stopping if population scores remains the same after generating molecules
            num_sims: number of times to traverse the tree,
            max_children: maximum number of childerns a node could have ,
            max_atoms: maximum number of atoms to explore to terminal the node state,
            pickle_directory: path from where to load pickle files
        """
        self.init_smiles = init_smiles
        self.pickle_directory = pickle_directory
        self.population_size = population_size
        self.max_children = max_children
        self.n_jobs = n_jobs
        self.num_sims = num_sims
        self.generations = generations
        self.patience = patience
        self.max_atoms = max_atoms

    def get_generator(self) -> GB_MCTS_Generator:
        """
        used for creating an instance of the GB_MCTS_Generator

        Returns:
            An instance of GB_MCTS_Generator
        """
        optimiser = GB_MCTS_Generator(
            pickle_directory=self.pickle_directory,
            init_smiles=self.init_smiles,
            population_size=self.population_size,
            max_children=self.max_children,
            num_sims=self.num_sims,
            generations=self.generations,
            n_jobs=self.n_jobs,
            max_atoms=self.max_atoms,
            patience=self.patience,
        )
        return optimiser
