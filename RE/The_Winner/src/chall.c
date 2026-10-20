
#include <stdio.h>
#include <string.h>
#include <gmp.h>

#define WIDTH 1024
#define MAX_INPUT 256

void rol(mpz_t out, const mpz_t val, unsigned int r, unsigned int width) {
    mpz_t a, b, mask;
    mpz_inits(a, b, mask, NULL);

    r %= width;
    mpz_set_ui(mask, 1);
    mpz_mul_2exp(mask, mask, width);
    mpz_sub_ui(mask, mask, 1);

    mpz_mul_2exp(a, val, r);
    mpz_fdiv_q_2exp(b, val, width - r);
    mpz_ior(out, a, b);
    mpz_and(out, out, mask);

    mpz_clears(a, b, mask, NULL);
}

void ror(mpz_t out, const mpz_t val, unsigned int r, unsigned int width) {
    mpz_t a, b, mask;
    mpz_inits(a, b, mask, NULL);

    r %= width;
    mpz_set_ui(mask, 1);
    mpz_mul_2exp(mask, mask, width);
    mpz_sub_ui(mask, mask, 1);

    mpz_fdiv_q_2exp(a, val, r);
    mpz_mul_2exp(b, val, width - r);
    mpz_ior(out, a, b);
    mpz_and(out, out, mask);

    mpz_clears(a, b, mask, NULL);
}

int main(void) {
    mpz_t N, e, c, input_m, result;
    mpz_inits(N, e, c, input_m, result, NULL);

    mpz_set_str(N,
        "82005629587362085999936531849166725807812331690781600555392779833296291674838653287419275819612138658412927203951982815363936615826012936754276519477737018435198301546777793531839893569990658220226999113285082152904547508234893614095384345329948167011137202799928546152025360764093632307447418606653555572893",
        10);

    mpz_set_str(e,
        "108214689647174422890042613001928827385730724529975507672044824861351446512648112464187206709045747962995844478081326844055906986333538167359318695480043717232773850876378659775631540441348113118997688923584173490132980549282940224091793551680394768233252823346730133716776487533555937796674157646968923168532",
        10);

    mpz_set_str(c,
        "1532057528837208481425042062909834366941136020506216780988751409963226985911000350064391015166917815064847885989185356084234467221019899273490540298846730112030042798096832563907497796821376639986513805222896140502939451205073354839377181877031939381364192634733256814016763130583014746330476194109134510358",
        10);

    ror(N, N, 3, WIDTH);
    rol(e, e, 4, WIDTH);
    rol(c, c, 7, WIDTH);

    char password[MAX_INPUT];

    printf("Enter the password: ");
    if (!fgets(password, sizeof(password), stdin)) {
        puts("Input error.");
        goto cleanup;
    }

    password[strcspn(password, "\r\n")] = '\0';

    mpz_import(input_m, strlen(password), 1, 1, 1, 0, password);

    mpz_powm(result, input_m, e, N);

    if (mpz_cmp(result, c) == 0) {
        puts("You win!");
    } else {
        puts("Try again.");
    }

cleanup:
    mpz_clears(N, e, c, input_m, result, NULL);
    return 0;
}
