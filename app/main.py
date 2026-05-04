from app.config import KNIGHTS
from app.knight import Knight
from app.battle import Battle


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle1 = Battle([lancelot, mordred])
    battle1.run_duel(rounds=1)

    # 2 Arthur vs Red Knight:
    battle2 = Battle([arthur, red_knight])
    battle2.run_duel(rounds=1)

    return {
        lancelot.name: lancelot.get_hp(),
        arthur.name: arthur.get_hp(),
        mordred.name: mordred.get_hp(),
        red_knight.name: red_knight.get_hp(),
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
