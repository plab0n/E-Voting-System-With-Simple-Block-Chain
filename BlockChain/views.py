from django.shortcuts import render

# Create your views here.

# !/usr/bin/env python
# coding: utf-8

# In[1]:

from django.shortcuts import render
from django.shortcuts import render
import os

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings as django_settings
from PIL import Image
import datetime
from django.conf import settings
from nomination.models import Nomination


# generates timestamps
import datetime
# contains hashing algorithms
import hashlib

from collections import namedtuple

# MyStruct = namedtuple("MyStruct", "fromuser touser position")
#
#
# # In[2]:
#
#
# # defining the 'block' data structure
# class Block:
#     # each block has 7 attributes
#
#     # 1 number of the block
#     blockNo = 0
#     # 2 what data is stored in this block?
#     data = None
#     # 3 pointer to the next block
#     next = None
#     # 4 The hash of this block (serves as a unique ID and verifies its integrity)
#     # A hash is a function that converts data into a number within a certain range.
#     hash = None
#     # 5 A nonce is a number only used once
#     nonce = 0
#     # 6 store the hash (ID) of the previous block in the chain
#     previous_hash = 0x0
#
#     # listofvotes = []
#     # 7 timestamp
#     timestamp = datetime.datetime.now()
#
#     # We initialize a block by storing some data in it
#     def __init__(self, fromuser, to, position):
#         m = MyStruct(fromuser=fromuser, touser=to, position=position)
#         self.data = m  # = MyStruct(fromuser, to, position )
#
#     # Function to compute 'hash' of a block
#     # a hash acts as both a unique identifier
#     # & verifies its integrity
#     # if someone changes the hash of a block
#     # every block that comes after it is changed
#     # this helps make a blockchain immutable
#     def hash(self):
#         # SHA-256 is a hashing algorithm that
#         # generates an almost-unique 256-bit signature that represents
#         # some piece of text
#         h = hashlib.sha256()
#         # the input to the SHA-256 algorithm
#         # will be a concatenated string
#         # consisting of 5 block attributes
#         # the nonce, data, previous hash, timestamp, & block #
#         h.update(
#             str(self.nonce).encode('utf-8') +
#             str(self.data.position).encode('utf-8') +
#             str(self.data.fromuser).encode('utf-8') +
#             str(self.data.touser).encode('utf-8') +
#             str(self.previous_hash).encode('utf-8') +
#             str(self.timestamp).encode('utf-8') +
#             str(self.blockNo).encode('utf-8')
#         )
#         # returns a hexademical string
#         return h.hexdigest()
#
#         ## SHOW DEMO 2, change data
#
#     def __str__(self):
#         # print out the value of a block
#         return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Voter: " + str(
#             self.data.touser) + "\nVoted For: " + str(self.data.fromuser) + "\nPosition: " + str(
#             self.data.position) + "\nHashes: " + str(self.nonce) + "\n--------------"
#
#
# #    def give_vote(self,candidate,position):
# #       for x in self.listofvotes:
#
# # print(x)
#
# #      return 0
#
# # In[3]:
#
#
# # defining the blockchain datastructure
# # consists of 'blocks' linked together
# # to form a 'chain'. Thats why its called
# # 'blockchain'
# class Blockchain:
#     # mining difficulty
#     diff = 20
#     # 2^32. This is the maximum number
#     # we can store in a 32-bit number
#     maxNonce = 2 ** 32
#     # target hash, for mining
#     target = 2 ** (256 - diff)
#
#     # generates the first block in the blockchain
#     # this is called the 'genesis block'
#     block = Block("foo", "bar", "baz")
#     # sets it as the head of our blockchain
#     head = block
#
#
#     # adds a given block to the chain of blocks
#     # the block to be added is the only parameter
#     def add(self, block):
#
#         temp = self.head
#
#         while (temp != self.block):
#             if (temp.data.fromuser == block.data.fromuser and temp.data.position == block.data.position):
#                 # error
#                 return -1
#             temp = temp.next
#
#         if (temp.data.fromuser == block.data.fromuser and temp.data.position == block.data.position):
#             # error
#             return -1
#
#         # set the hash of a given block
#         # as our new block's previous hash
#         block.previous_hash = self.block.hash()
#         # set the block # of our new block
#         # as the given block's # + 1, since
#         # its next in the chain
#         block.blockNo = self.block.blockNo + 1
#
#         # set the next block equal to
#         # itself. This is the new head
#         # of the blockchain
#         self.block.next = block
#         self.block = self.block.next
#
#         return block.data.touser
#
#
#
#     # Determines whether or not we can add a given block to
#     # the blockchain
#     def mine(self, block):
#         # from 0 to 2^32
#         for n in range(self.maxNonce):
#             # is the value of the given block's hash less than our target value?
#             if int(block.hash(), 16) <= self.target:
#                 # if it is,
#                 # add the block to the chain
#                 self.add(block)
#                 print(block)
#                 break
#             else:
#                 block.nonce += 1

    ## Show demo 3 ! Mine a block


# In[ ]:


# initialize blockchain
# blockchain = Blockchain()

# mine 10 blocks
# for n in range(10):
#     blockchain.add(Block(str(n), str(10 - n), "president"))
#
# blockchain.add(Block(str(9), str(1), "vice president"))
#
# # print out each block in the blockchain
# while blockchain.head != None:
#     print(blockchain.head)
#     blockchain.head = blockchain.head.next

# In[ ]:


# !/usr/bin/env python
# generates timestamps
import datetime
# contains hashing algorithms
import hashlib
from nomination.models import Category
from superadmin.models import Scheme

class Block(object):

    def __init__(self, block_no, data, previous_hash):
        self.block_no = block_no
        self.nonce = 0
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data['position']).encode('utf-8') +
            str(self.data['voted_by']).encode('utf-8') +
            str(self.data['voted_to']).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.block_no).encode('utf-8')
        )
        # returns a hexademical string
        return h.hexdigest()


    def __str__(self):
        # print out the value of a block
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.block_no) + "\nBlock Voter: " + str(
            self.data['voted_by']) + "\nVoted For: " + str(self.data['voted_to']) + "\nPosition: " + str(
            self.data['position']) + "\nPreviousHashe: " + str(self.previous_hash) + "\n--------------"


class Blockchain:

    def __init__(self):
        self.difficulty = 2
        self.chain = [Block(0, {"voted_by": "me", "voted_to": "you", "position": "ps"}, 0)]

    def add_block(self, data):
        for e in self.chain:
            if e.data['voted_by'] == data['voted_by'] and e.data['position'] == data['position']:
                # error
                return False

        previous_hash = self.chain[-1].hash()
        new_block = Block(len(self.chain), data, previous_hash)
        proof = self.proof_of_work(new_block)

        if self.valid_proof(new_block, proof):
            self.chain.append(new_block)
            self.last_hash = proof
        return True

    def valid_proof(self, block, proof):
        if block.hash() == proof:
            return True
        return False

    def proof_of_work(self, block):
        init_pattern = '0' * self.difficulty
        new_hash = block.hash()
        while not new_hash.startswith(init_pattern):
            block.nonce += 1
            new_hash = block.hash()
        return new_hash

    def is_valid(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i - 1].hash():
                print("Data of Block ", (i - 1), " changed")
                return False
            if self.last_hash != self.chain[-1].hash():
                print("Data of last Block changed")
                return False
        return True


    def print_chain(self):
        for e in self.chain:
            print(e)

    def is_voted_by(self, user_name):
        return [e.data['voted_to'] for e in self.chain if e.data['voted_by'] == user_name]

    def get_current_result(self):
        res ={}
        for i in range(1,len(self.chain)):
            # find the dict of a specific category
            if self.chain[i].data['position'] in res.keys():
                print("in")
                # find the candidate in the category dict
                if self.chain[i].data['voted_to'] in res[self.chain[i].data['position']].keys():
                    res[self.chain[i].data['position']][self.chain[i].data['voted_to']] += 1
                else:
                    res[self.chain[i].data['position']][self.chain[i].data['voted_to']] = 1
            else:
                res[self.chain[i].data['position']] = {}
                res[self.chain[i].data['position']][self.chain[i].data['voted_to']] = 1

        return res


def vote_home(request):
    return render(request, 'blockchain/vote_home.html')

blockchain = Blockchain()

def vote(request, pk):

    category = Category.objects.get(pk=pk)
    scheme = Scheme.objects.get(pk=request.session['scheme'])

    print(scheme.START_TIME, datetime.datetime.now(), scheme.CUT_OFF_TIME)

    if scheme.START_TIME.replace(tzinfo=None) < datetime.datetime.now() < scheme.CUT_OFF_TIME.replace(tzinfo=None):
        print("asd")
        if request.method == "POST":
            who = request.user
            whom = request.POST.get('candidate')
            # _user = User.objects.filter(username=whom)[0]
            pos = category

            print(whom, pos)


            blockchain.add_block({"voted_by": request.user.username, "voted_to": whom, "position": pos.name})


            res =  blockchain.get_current_result()
                # print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
                # res = blockchain.get_current_result()
                # for k,v in res.items():
                #     print(k,"888888",v)
            print(".................................#######.........")
            print(blockchain.print_chain())

            messages.add_message(request, messages.SUCCESS, "Vote has been casted")



            return render(request, 'blockchain/vote_result.html', {
                'result': res,
            })
        else:
            obj = Nomination.objects.filter(pos=category)
            voted = blockchain.is_voted_by(request.user.username)
            print(voted)
            obj = obj.exclude(whom__username__in=voted)
            print(pk)

            print(len(obj))

            return render(request, 'blockchain/nomination.html', {
                'candidate': obj,
                'title': category,
            })
    else:
        return render(request, 'blockchain/nomination.html', {
            'time_over': 1,
            'title': category,
        })