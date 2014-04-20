from jsonrpc import ServiceProxy
import sys
import string

# ===== BEGIN USER SETTINGS =====
# if you do not set these you will be prompted for a password for every command
rpcuser = ""
rpcpass = ""
# ====== END USER SETTINGS ======


if rpcpass == "":
    access = ServiceProxy("http://127.0.0.1:8332")
else:
    access = ServiceProxy("http://"+rpcuser+":"+rpcpass+"@127.0.0.1:8332")

def arg_command(command, args):
    def f():
        try:
            inp = []
            for arg in args:
                inp.append(raw_input(arg))
            print(getattr(access, command)(*inp))
        except:
            print("\n---An error occurred---\n")
            sys.exit(1)
    return f
            
def optarg_command(command, args):
    def f():
        try:
            imp = []
            for arg in args:
                inp.append(raw_input(arg)
            try:
                print(getattr(access, command)(*inp))
            except:
                print(getattr(access, command)())
            sys.exit(0)
        except:
            print("\n---An error occurred---\n")
            sys.exit(1)
    return f
            
def simple_command(command):
    def f():
        try:
            print(getattr(access, command)())
            sys.exit(0)
        except:
            print("\n---An error occurred---\n")
            sys.exit(1)
    return f

backupwallet = arg_command("backupwallet", ["Enter destination path/filename: "])
getaccount = arg_command("getaccount", ["Enter a Bitcoin address: "])
getaccountbuyaddress = arg_command("getaccountaddress", ["Enter an account name: "])
getaddressesbyaccount = arg_command("getaddressesbyaccount", ["Enter an accout name: "])
getblockbycount = arg_command("getblockbycount", ["Height: "])
getbalance = optarg_command("getbalance", ["Enter an account (optional): ", "Minimum confirmations (optional): "])
getblockcount = simple_command("getblockcount")
getblocknumber = simple_command("getblocknumber")
getconnectioncount = simple_command("getconnectioncount")
getdifficulty = simple_command("getdifficulty")
getgenerate = simple_command("getgenerate")
gethashespersec = simple_command("gethashespersec")
getinfo = simple_command("getinfo")
getnewaddress = optarg_command("getnewaddress", ["Enter an account name: "])
getreceivedbyaccount = optarg_command("getreceivedbyaccount", ["Enter an account (optional): ", "Minimum confirmations (optional): "])
getreceivedbyaddress = optarg_command("getreceivedbyaddress", ["Enter a Bitcoin address (optional): ", "Minimum confirmations (optional): "])
gettransaction = arg_command("gettransaction", "Enter a transaction ID: ")
getwork = optarg_command("gettransaction", ["Data (optional): "])
help = optarg_command("help", ["Command (optional): "])
listaccounts = optarg_command("listaccounts", ["Minimum confirmations (optional): "])
listreceivedbyamount = optarg_command("listreceivedbyamount", ["Minimum confirmations (optional): ", "Include empty? (true/false, optional): "])
listreceivedbyaddress = optarg_command("listreceivedbyaddress", ["Minimum confirmations (optional): ", "Include empty? (true/false, optional): "])
listtransactions = optarg_command("listtransactions", ["Account (optional): ", "Number of transactions (optional): ", "Skip (optional):"])
def move():
    try:
        frm = raw_input("From: ")
        to = raw_input("To: ")
        amt = raw_input("Amount:")
        mc = raw_input("Minimum confirmations (optional): ")
        comment = raw_input("Comment (optional): ")
        try:
            print access.move(frm, to, amt, mc, comment)
        except:
            print access.move(frm, to, amt)
        sys.exit(0)
    except:
        print "\n---An error occurred---\n"
        sys.exit(1)
def sendfrom():
    try:
        frm = raw_input("From: ")
        to = raw_input("To: ")
        amt = raw_input("Amount:")
        mc = raw_input("Minimum confirmations (optional): ")
        comment = raw_input("Comment (optional): ")
        commentto = raw_input("Comment-to (optional): ")
        try:
            print access.sendfrom(frm, to, amt, mc, comment, commentto)
        except:
            print access.sendfrom(frm, to, amt)
        sys.exit(0)
    except:
        print "\n---An error occurred---\n"
        sys.exit(1)
def sendmany():
    try:
        frm = raw_input("From: ")
        to = raw_input("To (in format address1:amount1,address2:amount2,...): ")
        mc = raw_input("Minimum confirmations (optional): ")
        comment = raw_input("Comment (optional): ")
        try:
            print access.sendmany(frm,to,mc,comment)
        except:
            print access.sendmany(frm,to)
        sys.exit(0)
    except:
        print "\n---An error occurred---\n"
        sys.exit(1)
def sendtoaddress():
    try:
        to = raw_input("To (in format address1:amount1,address2:amount2,...): ")
        amt = raw_input("Amount:")
        comment = raw_input("Comment (optional): ")
        commentto = raw_input("Comment-to (optional): ")
        try:
            print access.sendtoaddress(to,amt,comment,commentto)
        except:
            print access.sendtoaddress(to,amt)
        sys.exit(0)
    except:
        print "\n---An error occurred---\n"
        sys.exit(1)
setaccount = arg_command("setaccount", ["Address: ", "Account: "])
def setgenerate():
    try:
        gen= raw_input("Generate? (true/false): ")
        cpus = raw_input("Max processors/cores (-1 for unlimited, optional):")
        try:
            print access.setgenerate(gen, cpus)
        except:
            print access.setgenerate(gen)
        sys.exit(0)
    except:
        print "\n---An error occurred---\n"
        sys.exit(1)
settxfee = arg_command("settxfee", "Amount: ")
stop = simple_command("stop")
validateaddress = arg_command("validateaddress")
def walletpassphrase():
    try:
        pwd = raw_input("Enter wallet passphrase: ")
        access.walletpassphrase(pwd, 60)
        print "\n---Wallet unlocked---\n"
    except:
        print "\n---An error occurred---\n"
walletpassphrasechange = arg_command("walletpassphrasechange", ["Enter old wallet passphrase: ", "Enter new wallet passphrase: "])









else:
    print "Command not found or not supported"
