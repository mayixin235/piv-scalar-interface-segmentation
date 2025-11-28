
function[layer1, layer2, layer3, layer4, layer5, line]=Layer_Generator()

%Velocimetry Particle Image Generator
clc
close all;
clear;

%PARAMETERS
width = 256;        % image size
p_width = 2;        % particle size
p_brightness = 0.9; % particle brightness
noise_mu = 0.01;     % background noise mean
noise_var = 0.01;   % background noise variance (white noise)




%generating particle locations and blank background
[p_locs1, p_locs2, p_locs3, p_locs4, p_locs5, line] = point_generator();


p_npoints1 = length(p_locs1);
p_npoints2 = length(p_locs2);
p_npoints3 = length(p_locs3);
p_npoints4 = length(p_locs4);
p_npoints5 = length(p_locs5);

bg1 = zeros(width+2*p_width,width+2*p_width);
bg2 = zeros(width+2*p_width,width+2*p_width);
bg3 = zeros(width+2*p_width,width+2*p_width);
bg4 = zeros(width+2*p_width,width+2*p_width);
bg5 = zeros(width+2*p_width,width+2*p_width);

p_dens = gaussian_2d(p_width);

%adding particles to base image

for i = 1:1:p_npoints1
   xrange1 = p_locs1(i,1):(p_locs1(i,1)+p_width);
   yrange1 = p_locs1(i,2):(p_locs1(i,2)+p_width);
   bg1(xrange1,yrange1) = bg1(xrange1,yrange1)+ p_dens;
end

for i = 1:1:p_npoints2
   xrange2 = p_locs2(i,1):(p_locs2(i,1)+p_width);
   yrange2 = p_locs2(i,2):(p_locs2(i,2)+p_width);
   bg2(xrange2,yrange2) = bg2(xrange2,yrange2)+ p_dens;
end

for i = 1:1:p_npoints3
   xrange3 = p_locs3(i,1):(p_locs3(i,1)+p_width);
   yrange3 = p_locs3(i,2):(p_locs3(i,2)+p_width);
   bg3(xrange3,yrange3) = bg3(xrange3,yrange3);%+ p_dens;
end

for i = 1:1:p_npoints4
   xrange4 = p_locs4(i,1):(p_locs4(i,1)+p_width);
   yrange4 = p_locs4(i,2):(p_locs4(i,2)+p_width);
   bg4(xrange4,yrange4) = bg4(xrange4,yrange4)+ p_dens;
end

for i = 1:1:p_npoints5
   xrange5 = p_locs5(i,1):(p_locs5(i,1)+p_width);
   yrange5 = p_locs5(i,2):(p_locs5(i,2)+p_width);
   bg5(xrange5,yrange5) = bg5(xrange5,yrange5)+ p_dens;
end

%cropping, adjusting brightness, adding noise
noiseless1 = bg1(p_width+1:end-p_width,p_width+1:end-p_width)*p_brightness*(p_width^2);
layer1 = imnoise(noiseless1,'gaussian',noise_mu,noise_var);
%imagesc(layer1);
%colormap gray
%axis equal
%imwrite(final,'im1.png');

noiseless2 = bg2(p_width+1:end-p_width,p_width+1:end-p_width)*p_brightness*(p_width^2);
layer2 = imnoise(noiseless2,'gaussian',noise_mu,noise_var);


noiseless3 = bg3(p_width+1:end-p_width,p_width+1:end-p_width)*p_brightness*(p_width^2);
layer3 = imnoise(noiseless3,'gaussian',noise_mu,noise_var);


noiseless4 = bg4(p_width+1:end-p_width,p_width+1:end-p_width)*p_brightness*(p_width^2);
layer4 = imnoise(noiseless4,'gaussian',noise_mu,noise_var);
%imagesc(layer2);
%colormap gray
%axis equal
%imwrite(final,'im1.png');

noiseless5 = bg5(p_width+1:end-p_width,p_width+1:end-p_width)*p_brightness*(p_width^2);
layer5 = imnoise(noiseless5,'gaussian',noise_mu,noise_var);

end

function [gauss_2d] = gaussian_2d(width)
%generates 2d gaussian distribution
mu = [width/2 width/2]; sigma = [width/2 width/2];
[X1,X2] = meshgrid(0:1:width,0:1:width);
X = [X1(:),X2(:)];
gauss_2d = mvnpdf(X,mu,sigma);
gauss_2d = reshape(gauss_2d,width+1,width+1);

end

function [p_1, p_2, p_3, p_4, p_5, line]= point_generator()
[~, points1] = Im_Generator() %create layer 1 particle image
[~, points2] = Im_Generator(); %create layer 2 particle image
[~, points3] = Im_Generator(); %create layer 3 particle image
[~, points4] = Im_Generator(); %create layer 4 particle image
[~, points5] = Im_Generator(); %create layer 5 particle image

[line] = Line_Generator(); 
line = line + 128; %create random line + 128 bc of positioning of the line


    for pt = 1:1:1500
        a1 = points1(pt, 2); %X value of the point
        b1 = points1(pt, 1);%Y value of the point
        
        a2 = points2(pt, 2); 
        b2 = points2(pt, 1);
        
        a3 = points3(pt, 2); 
        b3 = points3(pt, 1);      
        
        a4 = points4(pt, 2); 
        b4 = points4(pt, 1);
        
        a5 = points5(pt, 2); 
        b5 = points5(pt, 1);
        
   for i = 1:1:256
            c = line(i,1); %i is the x point and c is the y point of the line
            
            if a1 == i && b1 < c
                    points1(pt,:)= 0;
            end
            
            if a2 == i && b2 < c
                    points2(pt,:)= 0;
            end
            
            if a3 == i && b3 < c
                    points3(pt,:)= 0;
            end
            
            if a4 == i && b4 < c
                    points4(pt,:)= 0;
            end
             
            if a5 == i && b5 < c
                    points5(pt,:)= 0;
            end
        end
    end
    
    p_1 = points1
    p_1(any(points1==0,2),:) = []
    
    p_2 = points2;
    p_2(any(points2==0,2),:) = [];
    
    p_3 = points3;
    p_3(any(points3==0,2),:) = [];
    
    p_4 = points4;
    p_4(any(points4==0,2),:) = [];
    
    p_5 = points5;
    p_5(any(points5==0,2),:) = [];
    
end

function[Res]=Line_Generator()
%generate ground truth line
clear
clc

N=50;
Nx=256;
LwLim=600; % lower limit of A
UpLim=200; % upper limit of A
Lwk=100;   % lower limit of wavelength
Upk=250;    % upper limit of wavelength
shft=10;    % total shift +/- shft pixels

x=1:1:Nx;
Res=zeros(size(x));

A=sort(rand(N,1)*(UpLim-LwLim)+LwLim,1);
Lam=sort(rand(N,1)*(Upk-Lwk)+Lwk,1); %WAVELENGTH
B=2*pi./Lam; 
C=(rand(N,1)*2-1)*pi; % -pi to pi
D=rand(N,1)*2*shft-shft; 

for i=1:N
    Res= Res+A(i)*sin(B(i)*x+C(i))+D(i);
end

Res=[Res/N+rand(1,1)*2*shft-shft]'

end
