
from person_model import PersonModel


if __name__ == "__main__":
    personModel = PersonModel(50)

    for i in range(50):
        personModel.step()
        print("\n ---------------- Iteration " +
              str(i + 1) + " ---------------- \n")
