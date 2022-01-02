

def convert_if(args):
    convert_if.node_list=[]
    cond = ""


    for key,value in args.items():

        if key == "cond":
            if type(value) is dict:
                node_list=loop_cond(value)
                for i in node_list:
                    cond=cond+i
    print(cond)








def loop_cond(args):
    for key, value in args.items():
        if key == "left":
            if value["_nodetype"] == "ID":
                name = value["name"]
                convert_if.node_list.append(name)

            elif value["_nodetype"] == "Constant":

                val = value["value"]
                convert_if.node_list.append(val)
            else:
                loop_cond(value)

        else:
            if key == "op":
                op = value
                convert_if.node_list.append(op)
            elif key == "right":

                if value["_nodetype"] == "ID":
                    name = "&" + value["name"]
                    convert_if.node_list.append(name)

                else:

                    val = value["value"]
                    convert_if.node_list.append(val)
            elif key == "value":

                val = value
                convert_if.node_list.append(val)

    return (convert_if.node_list)