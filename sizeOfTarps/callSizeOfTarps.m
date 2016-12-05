clear all; close all; clc;

data10 = csvread('AltitudeVsDriftUppperSection.csv',4,0);
data20 = csvread('AltitudeVsDriftUperSection20mph.csv',4,0);


resolution = 8; %MP
fovHorizontal = 48.8;%degrees
fovVertical = 62.2; %degrees
altitude = linspace(.0001,5500,1000); %ft
range = linspace(.0001, 2500,1001); %ft

numPixels = zeros(length(altitude),length(range));

for i = 1:length(altitude)
    for j = 1:length(range)
        numPixels(i,j) = sizeOfTarps(altitude(i),range(j),resolution,fovHorizontal,fovVertical);
    end
end

range = linspace(-2500,2500,2001);

for i = 1:length(altitude)
    for j = 1:length(range)
        if (j<1001)
            numPixels2(i,j) = numPixels(i,1002-j);
        else
            numPixels2(i,j) = numPixels(i,j-1000);
        end
        if(sqrt(i^2 + (j-1001)^2) < 50)
            numPixels2(i,j) = NaN;
        end
    end
end
v = [300, 500, 800, 1200, 1700, 2300, 3000, 4000, 6000, 20000];
[C,h] = contour(range,altitude,numPixels2,v);
hold on;
plot(data10(:,2),data10(:,1),'Linewidth',4)
plot(data20(:,2),data20(:,1),'Linewidth',4)
clabel(C,h,v)
xlabel('Downrange Distance [ft]')
ylabel('Altitude [ft]')
legend('Contours of Tarp Size in Pixels','10 MPH Wind Trajectory','20 MPH Wind Trajectory')
% title('Estimated Number of Pixels Occupied by Tarp')
set(gca,'FontSize',16)
%testing github