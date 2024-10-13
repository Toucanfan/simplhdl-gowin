import cocotb
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

async def wait_cycles(clk, num):
    for i in range(num):
        await RisingEdge(clk)

@cocotb.test()
async def test(dut):
    c = Clock(dut.clk, 10, 'ns')
    await cocotb.start(c.start())

    await Timer(1000, 'ms')
