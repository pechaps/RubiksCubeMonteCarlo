import os
import time

from rubiks_cube import RubiksCube

from multiprocessing import Pool
import numpy as np
import pandas as pd


def random_solve(random_seed: int) -> int:
    """
    Select a movement randomly to be performed on the cube.
    Returns the number of movement required to go back to the initial state
    """
    np.random.seed(random_seed)

    rubik_movement = [
        lambda x: x.move_up(),
        lambda x: x.move_up_inverse(),
        lambda x: x.move_right(),
        lambda x: x.move_right_inverse(),
        lambda x: x.move_front(),
        lambda x: x.move_front_inverse(),
    ]

    rubik = RubiksCube()

    random_move = np.random.choice(rubik_movement)
    random_move(rubik)
    number_of_mvt = 1
    while rubik.is_cube_resolved(rubik.state) is False:
        random_move = np.random.choice(rubik_movement)
        random_move(rubik)
        number_of_mvt += 1
    return number_of_mvt


if __name__ == "__main__":

    # Use of multiprocessing to make the whole stuff faster. Results are stored in a csv file.

    N = 1000

    start_time = time.perf_counter()
    with Pool() as pool:
        results = pool.map(random_solve, range(N))
    finish_time = time.perf_counter()

    print(f"Computation time : {finish_time - start_time}s")

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    results_df = pd.DataFrame({"#Movement": results})
    results_df.to_csv(f"{output_dir}/results_{N}.csv")
