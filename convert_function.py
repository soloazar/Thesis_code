import convert_int as int_convertor
import convert_char as char_convertor
import convert_float as float_convertor
import convert_double as double_convertor
import convert_statement as statement_convertor
import convert_array as array_convertor
from write_to_rust_file import write_to_rust_file


def convert_function(args):
    node_list = []
    func = "fn" + " " + args["decl"]["name"] + "(" + ")" + "{"
    write_to_rust_file(func,'a')

    print(func)
    for i,j in args.items():
        if i=="body":
            for key, value in j.items():
                if key=="block_items":
                    get_all_values(key,value)
                    write_to_rust_file("}",'a')

                    print("\n}")






def get_dict_values(parent,args):
    global nodetype
    for key,value in args.items():
        if key=="stmt":
            pass
        else:
            if type(value) != dict and type(value) != list:
                a = 2
                # print(key,":",value)

                if key == "_nodetype":
                    nodetype = key






            elif type(value) is list:
                get_all_values(key, value)
            elif type(value) is dict:
                    # print(key,"--")

                get_dict_values(key, value)


def get_all_values(key, args):
    result=""
    list_len=len(args)
    iteration_number=0
    for i in args:
        iteration_number+=1
        if type(i) != dict and type(i) != list:
            # print(key,":",i)

            a = 1


        elif type(i) is dict:
            #if i["_nodetype"] == "For":
             #   convert_for(i)

            if i["_nodetype"] == "Decl":
                if i["type"]["_nodetype"] == "TypeDecl":

                    for j in i["type"]["type"]["names"]:

                        if j == "int":
                            result=int_convertor.convert_int(i)

                        elif j == "char":
                            char_convertor.convert_char(i)
                        elif j == "float":
                            float_convertor.convert_float(i)
                        elif j == "double":
                            double_convertor.convert_double(i)
                elif i["type"]["_nodetype"] == "ArrayDecl":
                    array_convertor.convert_array(i)

            elif i["_nodetype"] == "Assignment":
                result=statement_convertor.convert_statement(i)
            get_dict_values(key, i)





        elif type(i) is list:
            get_all_values(key, i)
        #print(result)
        #if iteration_number==list_len:
          #  print("")
    return (result)
