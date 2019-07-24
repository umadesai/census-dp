from laplace import laplace_mech


def dp_mean(eps_n, eps_d, top, bot, top_sen=100.0, bot_sen=1.0):
    noisy_top = laplace_mech(top, eps_n, top_sen)
    noisy_bot = laplace_mech(bot, eps_d, bot_sen)
    return noisy_top / noisy_bot
