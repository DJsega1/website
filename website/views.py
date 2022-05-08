from website import app


@app.route("/5up3r_s3cr3t_34st3r_egg")
def test_view():
    return "flag{w0w_y0u_f1nd_m3}"
