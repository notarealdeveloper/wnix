#!/usr/bin/env python3


def test_coreutils():

    import numpy as np
    from wnix import Sims, What, Attn, Grep, Sed

    colors  = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    animals = ['horse', 'cow', 'chicken', 'pig']
    strange = ['sky bovine', 'rouge bull', 'grass poultry', 'lemon rooster']
    french_colors = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'violet']

    #query = strange
    #keys  = animals
    #S = Sims(query, keys)   # dim_q, dim_k
    #W = What(query, keys)   # dim_k, dim_q
    #A = Attn(query, keys)   # dim_q, embed_dim
    #G = Grep(query, keys)   # dim_k, dim_q

    inputs = strange
    search = animals
    G = Grep(inputs, search)
    assert np.all(G[0] == ['cow', 'cow', 'chicken', 'chicken'])

    inputs = strange
    search = colors
    G = Grep(inputs, search)
    assert np.all(G[0] == ['blue', 'red', 'green', 'yellow'])

    inputs  = strange
    search  = colors
    replace = french_colors
    S = Sed(inputs, search, replace)
    assert np.all(S[0] == ['bleu', 'rouge', 'vert', 'jaune'])

    inputs = strange
    search = animals
    G = Grep(inputs, search)
    assert np.all(G[0] == ['cow', 'cow', 'chicken', 'chicken'])

    if False:
        # Move these to the shell test
        cmd = "cat etc/lines/colors.%s | Grep etc/colors"
        assert os.popen(cmd % 'easy').read().splitlines() == colors
        assert os.popen(cmd % 'medium').read().splitlines() == colors
        assert os.popen(cmd % 'hard').read().splitlines() == colors

        #product colors animals | Sed colors colors.french
        #paste colors animals | head -6 | Sed colors.french colors.german
        #cat colors | Sed colors.french colors.german
        colors_hungarian = ['piros', 'narancssárga', 'sárga', 'zöld', 'kék', 'lila']
        pipe = os.popen('cat etc/colors | Sed etc/colors.french etc/colors.hungarian')
        assert pipe.read().splitlines() == colors_hungarian



test_coreutils()
