def solve_bs_pde(s0,smax,k,T,N,M,sig,r,p):
    
    ht = T/N
    hs = smax/M
    t = np.arange(0, T+ht, ht)
    s = np.arange(0, smax+hs, hs)
    
    d = 1-(sig**2)*(s**2)*ht/(hs**2)-r*ht
    l = 0.5*(sig**2)*(s**2)*ht/(hs**2)-r*s*ht/(2*hs)
    u = 0.5*(sig**2)*(s**2)*ht/(hs**2)+r*s*ht/(2*hs)
    
    A = np.matrix(np.zeros((M-1,M-1)))
    diag = d[1:]
    upperDiag = u[1:M-1]
    lowerDiag = l[2:M]
    for i in range(len(upperDiag)):
        A[i,i+1] = upperDiag[i]
        A[i+1,i] = lowerDiag[i]
    for i in range(M-1):
        A[i,i] = diag[i]
    vec_eigenvalue = np.linalg.eigvals(A)
    
    b = u[M-1]*(s[M]-k*np.exp(-r*(T-t)))
    #ba = u[M-1]*(s[M]-k)

    diff = s-k
    diff[diff<0]=0
    ter_c = np.matrix(diff[1:M]).T
    cont_val = ter_c

    for i in range(N, 1, -1):
        bb = np.append(np.zeros(M-2),b[i]).reshape(M-1,1)
        exercise_val =  np.maximum(s[1:-1]-k, np.zeros(M-1)).reshape(M-1,1)
        cont_val = A @ cont_val + bb
        # exercise if exercise value exceeds continuation value
        vec_c = np.maximum(cont_val, exercise_val)
        
    return vec_c