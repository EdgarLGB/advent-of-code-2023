input = r"""
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

input2 = r"""
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

input3 = r"""
%zl -> zp, cl
%vp -> dj, vr
%cc -> xp
&dj -> lq, mb, dc, ns, gz
%md -> ts, zp
%fc -> zp
%px -> zx
&nx -> gl, br, pr, xf, vd, gj, kd
%tf -> lt, dj
%fj -> pc
%mb -> xx
%cl -> mj
%pm -> fj
%dc -> dj, vp
%jc -> bz, xm
&vd -> zh
%pz -> sr, nx
&ns -> zh
%sr -> nx
%gl -> pr
%xx -> nt, dj
%gp -> md
%hb -> jl, nx
&zh -> rx
%rb -> gz, dj
%xm -> bz
&zp -> px, gp, cl, bh, fn, ls, hs
&bz -> pm, pc, bv, dl, jp, fj, cc
%nl -> bz, pm
&bh -> zh
%hq -> gj, nx
%bv -> bz, nl
%bj -> jp, bz
%gj -> mx
%xp -> bz, bj
%vr -> dj, mb
&dl -> zh
%pr -> hb
%nt -> dj, lq
%mx -> gl, nx
%kd -> hq
%fn -> px
%jp -> xc
%zx -> zl, zp
%br -> nx, xf
%lt -> dj
%df -> dj, tf
%ts -> zp, fc
%jl -> nx, pz
%xc -> jc, bz
%xf -> kd
%lq -> rb
%gz -> df
%pc -> cc
%hs -> fn
broadcaster -> ls, bv, dc, br
%mj -> zp, gp
%ls -> hs, zp
"""

from dataclasses import dataclass, field


@dataclass
class Module:
    source_list: [] = field(default_factory=list)
    destination_list: [] = field(default_factory=list)
    module_list: {} = field(default_factory=dict)

    def add_destination(self, name):
        self.destination_list.append(name)

    def add_source(self, name):
        self.source_list.append(name)

    def add_module_list(self, module_list):
        self.module_list = module_list

    def output(self, input, source_name):
        pass


@dataclass
class Broadcaster(Module):
    def output(self, input, source_name):
        return input


@dataclass
class FlipFlop(Module):
    state: bool = False

    def output(self, input, source_name):
        if input == False:
            self.state = not self.state
            return self.state


@dataclass
class Conjunction(Module):
    state: [] = field(default_factory=list)

    def add_source(self, name):
        super().add_source(name)
        self.state.append(False)

    def output(self, input, source_name):
        self.state[self.source_list.index(source_name)] = input
        number_of_high_state = 0
        for remembered_signal in self.state:
            if remembered_signal:
                number_of_high_state += 1
        return number_of_high_state != len(self.state)


import re


def decode(input):
    all_modules = {}
    lines = input.strip().split("\n")
    for line in lines:
        line_parts = line.split(" -> ")
        source_name = line_parts[0]
        source = None
        if source_name == "broadcaster":
            source = Broadcaster()
        elif "%" in source_name:
            source = FlipFlop()
            source_name = source_name[1:]
        elif "&" in source_name:
            source = Conjunction()
            source_name = source_name[1:]
        all_modules[source_name] = source

    for line in lines:
        line_parts = line.split(" -> ")
        source_name = re.findall("\w+", line_parts[0])[0]
        source = all_modules[source_name]
        source.add_module_list(all_modules)

        destination_name_list = line_parts[1].split(", ")
        for destination_name in destination_name_list:
            source.add_destination(destination_name)
            if destination_name not in all_modules:
                continue
            destination = all_modules[destination_name]
            destination.add_source(source_name)
    return all_modules


def push_button(all_modules):
    result = []
    queue = [("button", False, "broadcaster")]
    while len(queue) > 0:
        # print(queue)
        source_name, input, module_name = queue.pop(0)
        result.append(input)
        if module_name not in all_modules:
            continue
        module = all_modules[module_name]
        output = module.output(input, source_name)
        if output == None:
            continue
        for destination_name in module.destination_list:
            queue.append((module_name, output, destination_name))
    return result


def play(input):
    all_modules = decode(input)
    high = 0
    low = 0
    for i in range(1000):
        result = push_button(all_modules)
        # print(result)
        for signal in result:
            if signal:
                high += 1
            else:
                low += 1
    print(f"high={high}")
    print(f"low={low}")
    return high * low


print(play(input))
print(play(input2))
print(play(input3))


###### Part two ######
def push_button_2(all_modules):
    queue = [("button", False, "broadcaster")]
    while len(queue) > 0:
        # print(queue)
        source_name, input, module_name = queue.pop(0)
        if module_name == 'rx' and input == False:
            return True
        if module_name not in all_modules:
            continue
        module = all_modules[module_name]
        output = module.output(input, source_name)
        if output == None:
            continue
        for destination_name in module.destination_list:
            queue.append((module_name, output, destination_name))
    return False


def play_2(input):
    all_modules = decode(input)
    i = 0
    while True:
        i += 1
        if i % 100 == 0:
            print(f'i={i}')
        if push_button(all_modules) == True:
            return i

print(play_2(input3))