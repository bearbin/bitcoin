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
cmd = sys.argv[1].lower()

def arg_command(command, args):
    if sys.argv[1].lower() == command:
        try:
            imp = []
            for arg in args:
                inp.append(raw_input(arg)
            print(getattr(access, command)(*inp))
            sys.exit(0)
        except:
            print("\n---An error occurred---\n")
            sys.exit(1)
            
def optarg_command(command, args):
    if sys.argv[1].lower() == command:
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
            
def simple_command(command):
    if sys.argv[1].lower() == command:
        try:
            print(getattr(access, command)())
            sys.exit(0)
        except:
            print("\n---An error occurred---\n")
            sys.exit(1)

arg_command("backupwallet", ["Enter destination path/filename: "])
arg_command("getaccount", ["Enter a Bitcoin address: "])
arg_command("getaccountaddress", ["Enter an account name: "])
arg_command("getaddressesbyaccount", ["Enter an accout name: "])
arg_command("getblockbycount", ["Height: "])
optarg_command("getbalance", ["Enter an account (optional): ", "Minimum confirmations (optional): "])
simple_command("getblockcount")
simple_command("getblocknumber")
simple_command("getconnectioncount")
simple_command("getdifficulty")
simple_command("getgenerate")
simple_command("gethashespersec")
simple_command("getinfo")
optarg_command("getnewaddress", ["Enter an account name: "])
optarg_command("getreceivedbyaccount", ["Enter an account (optional): ", "Minimum confirmations (optional): "])
optarg_command("getreceivedbyaddress", ["Enter a Bitcoin address (optional): ", "Minimum confirmations (optional): "])
arg_command("gettransaction", "Enter a transaction ID: ")
if cmd == "getwork":
    try:
        data = raw_input("Data (optional): ")
        try:
            print access.gettransaction(data)
        except:
            print access.gettransaction()
    except:
        print "\n---An error occurred---\n"
optarg_command("help", ["Command (optional): "])
optarg_command("listaccounts", ["Minimum confirmations (optional): "])
optarg_command("listreveivedbyamount", ["Minimum confirmations (optional): ", "Include empty? (true/false, optional): "])
optarg_command("listreceivedbyaddress", ["Minimum confirmations (optional): ", "Include empty? (true/false, optional): "])
optarg_command("listtransactions", ["Account (optional): ", "Number of transactions (optional): ", "Skip (optional):"])
arg_command("settxfee", "Amount: ")
simple_command("stop")
arg_command("validateaddress")
arg_command("walletpassphrasechange", ["Enter old wallet passphrase: ", "Enter new wallet passphrase: "])


if cmd == "move":
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
    except:
        print "\n---An error occurred---\n"

elif cmd == "sendfrom":
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
    except:
        print "\n---An error occurred---\n"

elif cmd == "sendmany":
    try:
        frm = raw_input("From: ")
        to = raw_input("To (in format address1:amount1,address2:amount2,...): ")
        mc = raw_input("Minimum confirmations (optional): ")
        comment = raw_input("Comment (optional): ")
        try:
            print access.sendmany(frm,to,mc,comment)
        except:
            print access.sendmany(frm,to)
    except:
        print "\n---An error occurred---\n"

elif cmd == "sendtoaddress":
    try:
        to = raw_input("To (in format address1:amount1,address2:amount2,...): ")
        amt = raw_input("Amount:")
        comment = raw_input("Comment (optional): ")
        commentto = raw_input("Comment-to (optional): ")
        try:
            print access.sendtoaddress(to,amt,comment,commentto)
        except:
            print access.sendtoaddress(to,amt)
    except:
        print "\n---An error occurred---\n"

elif cmd == "setaccount":
    try:
        addr = raw_input("Address: ")
        acct = raw_input("Account:")
        print access.setaccount(addr,acct)
    except:
        print "\n---An error occurred---\n"

elif cmd == "setgenerate":
    try:
        gen= raw_input("Generate? (true/false): ")
        cpus = raw_input("Max processors/cores (-1 for unlimited, optional):")
        try:
            print access.setgenerate(gen, cpus)
        except:
            print access.setgenerate(gen)
    except:
        print "\n---An error occurred---\n"

elif cmd == "settxfee":
    try:
        amt = raw_input("Amount:")
        print access.settxfee(amt)
    except:
        print "\n---An error occurred---\n"

elif cmd == "stop":
    try:
        print access.stop()
    except:
        print "\n---An error occurred---\n"

elif cmd == "validateaddress":
    try:
        addr = raw_input("Address: ")
        print access.validateaddress(addr)
    except:
        print "\n---An error occurred---\n"

elif cmd == "walletpassphrase":
    try:
        pwd = raw_input("Enter wallet passphrase: ")
        access.walletpassphrase(pwd, 60)
        print "\n---Wallet unlocked---\n"
    except:
        print "\n---An error occurred---\n"


else:
    print "Command not found or not supported"
