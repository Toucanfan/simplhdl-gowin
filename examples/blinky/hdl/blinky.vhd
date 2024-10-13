library ieee;

use ieee.std_logic_1164.all;
use ieee.numeric_std_unsigned.all;

entity blinky is
    generic (
        G_CNTR_WIDTH : integer := 24
    );
    port (
        clk : in  std_logic;
        led : out std_logic
    );
end entity blinky;

architecture rtl of blinky is

    signal counter : std_logic_vector(G_CNTR_WIDTH-1 downto 0) := (others => '0');

begin

counter_p : 
    process (clk) begin
        if rising_edge(clk) then
            counter <= counter + 1;
        end if;
    end process;

    led <= counter(counter'left);

end architecture rtl;
