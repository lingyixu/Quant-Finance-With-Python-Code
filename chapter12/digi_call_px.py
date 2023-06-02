def digi_call_px(k, rf, tau, nodes, probs, dk):
    digi_px = 0.0
    for zz, node_zz in enumerate(nodes):
        if node_zz >= k:
            digi_px += math.exp(-rf*tau) * probs[zz] * dk

    return digi_px
