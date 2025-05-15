import matplotlib


def build_cmap(minP=None,midP=None,maxP=None):
    if minP==None: hex_list_min=[]
    else: 
    #color1=mcp.gen_color(cmap="winter",n=5)
        cmap = matplotlib.cm.get_cmap(minP[1],len(minP[0])+1)
        hex_list_min=[]
        for i in range(cmap.N):
            rgba = cmap(i)
            # rgb2hex accepts rgb or rgba

            hex_list_min.append(matplotlib.colors.rgb2hex(rgba))

    
    cmap = matplotlib.cm.get_cmap(maxP[1],len(maxP[0])+1)
    hex_list_max=[]
    for i in range(cmap.N):
        rgba = cmap(i)
        # rgb2hex accepts rgb or rgba

        hex_list_max.append(matplotlib.colors.rgb2hex(rgba))

    if midP!=None:
        hex_list=hex_list_min[:-1] + [midP[1]] + hex_list_max[1::]
    else:
        hex_list=hex_list_min[:-1] + hex_list_max[1::]
    cmap = matplotlib.colors.ListedColormap(hex_list)

    return cmap