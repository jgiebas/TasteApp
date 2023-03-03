import datetime
import jwt

with open( "../AuthKey_8365RCBGSS.p8"  ) as f:
    secret = f.read()
    teamid = "KF6N87ZKLG"
    keyid  = "8365RCBGSS"
    alg    = "ES256"

    time_now = datetime.datetime.now()
    time_exp = datetime.datetime.now() + datetime.timedelta( hours = 48  )

    headers = {
        "alg": alg,
        "kid": keyid
    }

    payload = {
        "iss": teamid,
        "exp": int( time_exp.timestamp()  ),
        "iat": int( time_now.timestamp()  )
    }

    token = jwt.encode( payload, secret, algorithm = alg, headers = headers )

    print( token  );
